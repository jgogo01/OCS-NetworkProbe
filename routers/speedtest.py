from fastapi import APIRouter
import datetime
import speedtest
import netifaces
import os
from dotenv import load_dotenv

load_dotenv()

def bytesToMb(bytes):
    KB = 1024  # One Kilobyte is 1024 bytes
    MB = KB * 1024  # One MB is 1024 KB
    return int(bytes / MB)

def speedtestByInterface(interface):
    try:
        source = netifaces.ifaddresses(interface)[netifaces.AF_INET][0]['addr']
        st = speedtest.Speedtest(source_address=source)
        return st
    except KeyError:
        raise ValueError("Unable to connect NIC, please recheck the interface name.")
    except Exception as e:
        raise ValueError(str(e))

router = APIRouter()

@router.get("/speedtest")
async def main():
    status = 200
    message = "Welcome to OCS API Probe"
    data = {}

    try:
        lanST = speedtestByInterface(os.getenv("INTERFACE_LAN"))
    except Exception as e:
        lanST = None
        
    try:
        wlanST = speedtestByInterface(os.getenv("INTERFACE_WLAN"))
    except Exception as e:
        wlanST = None
        
    data = {
            "timeStamp": datetime.datetime.now(),
            "lan": {
                "src": lanST._source_address if lanST != None else None,
                "speedtest": {
                    "server": lanST.get_best_server() if lanST != None else None,
                    "download": bytesToMb(lanST.download()) if lanST != None else 0,
                    "upload": bytesToMb(lanST.upload()) if lanST != None else 0,
                }
            },
            "wlan": {
                "src": wlanST._source_address if wlanST != None else None,
                "speedtest": {
                    "server": wlanST.get_best_server() if wlanST != None else None,
                    "download": bytesToMb(wlanST.download()) if wlanST != None else 0,
                    "upload": bytesToMb(wlanST.upload()) if wlanST != None else 0,
                }
            }
        }

    return {
        "status": status,
        "message": message,
        "data": data
    }
