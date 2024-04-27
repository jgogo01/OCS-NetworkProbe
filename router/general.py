from fastapi import APIRouter
import psutil
from gpiozero import CPUTemperature
import os
import time

def get_ipaddress_by_interface(interface):
  #LAN IPV4 Address
  try:
    IPV4 = psutil.net_if_addrs()[interface][0].address
  except Exception as e:
    IPV4 = None
  #LAN IPV6 Address
  try:
    IPV6 = psutil.net_if_addrs()[interface][1].address
  except Exception as e:
    IPV6 = None
  return IPV4, IPV6

def get_cpu_temp():
  try:
    CPU_TEMP = CPUTemperature().temperature
  except Exception as e:
    CPU_TEMP = None
  return CPU_TEMP

router = APIRouter()
@router.get("/general")
async def main():
  status = 200
  message = "Welcome to OCS API Probe"
  data = {}
  
  try: 
    CPU_TEMP = get_cpu_temp()
    LAN_IPV4, LAN_IPV6 = get_ipaddress_by_interface(os.getenv("INTERFACE_LAN"))
    WIFI_IPV4, WIFI_IPV6 = get_ipaddress_by_interface(os.getenv("INTERFACE_WIFI"))
    
    data = {
        "system": {
          "cpu": {
          "core": psutil.cpu_count(logical=False),
          "thread": psutil.cpu_count(logical=True),
          "usage": psutil.cpu_percent(),
          "temperature": CPU_TEMP,
          },
          "ram": {
              "usage": psutil.virtual_memory().used,
              "available": psutil.virtual_memory().available,
              "total": psutil.virtual_memory().total,
          },
          "network": {
            "lan": {
              "ipv4": LAN_IPV4,
              "ipv6": LAN_IPV6,
            },
            "wifi": {
              "ipv4": WIFI_IPV4,
              "ipv6": WIFI_IPV6,
            }
          }
        },
        "uptime": time.time() - psutil.boot_time(),
        "location": {
          "latitude": os.getenv("LATITUDE"),
          "longitude": os.getenv("LONGITUDE"),
        }
      }
  except Exception as e:
    status = 500
    message = str(e)
    
  return {
    "status": status,
    "message": message,
    "data": data
  }
  