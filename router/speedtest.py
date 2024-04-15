from fastapi import APIRouter
from dotenv import load_dotenv, dotenv_values
import datetime
import speedtest
import psutil
import netifaces

def bytesToMb(bytes):
  KB = 1024 # One Kilobyte is 1024 bytes
  MB = KB * 1024 # One MB is 1024 KB
  return int(bytes/MB)

def speedtestByInterface(interface):
    try:
        source = netifaces.ifaddresses(interface)[netifaces.AF_INET][0]['addr']
        st = speedtest.Speedtest(source_address=source)
        return st
    except KeyError:
        raise ValueError("Unable to connect NIC, please recheck the interface name.")
    except Exception as e:
        raise ValueError(str(e))
    
#Load Environment
load_dotenv()
env = dotenv_values(".env")
router = APIRouter()

@router.get("/speedtest")
async def main():
    status = 200
    message = "Welcome to OCS API Probe"
    data = {}

    try:
        lanST = speedtestByInterface(env["INTERFACE_LAN"])
        wifiST = speedtestByInterface(env["INTERFACE_WIFI"])

        data = {
            "timeStamp": datetime.datetime.now(),
            "nic": list((psutil.net_if_addrs().keys())),
            "lan": {
                "src": lanST._source_address,
                "speedtest":{
                    "server": lanST.get_best_server(),
                    "download": bytesToMb(lanST.download()),
                    "upload": bytesToMb(lanST.upload()),
                }
            },
            "wifi": {
                "src": wifiST._source_address,
                "speedtest":{
                    "server": wifiST.get_best_server(),
                    "download": bytesToMb(wifiST.download()),
                    "upload": bytesToMb(wifiST.upload()),
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