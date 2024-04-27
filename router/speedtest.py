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
        wlanST = speedtestByInterface(os.getenv("INTERFACE_WLAN"))

        data = {
            "timeStamp": datetime.datetime.now(),
            "lan": {
                "src": lanST._source_address,
                "speedtest": {
                    "server": lanST.get_best_server(),
                    "download": bytesToMb(lanST.download()),
                    "upload": bytesToMb(lanST.upload()),
                }
            },
            "wlan": {
                "src": wlanST._source_address,
                "speedtest": {
                    "server": wlanST.get_best_server(),
                    "download": bytesToMb(wlanST.download()),
                    "upload": bytesToMb(wlanST.upload()),
                }
            }
        }
    except Exception as e:
        status = 500
        message = str(e)
        data = None

    return {
        "status": status,
        "message": message,
        "data": data
    }
