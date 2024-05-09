from fastapi import APIRouter
import psutil
import os
import time
from utils.general import *
from utils.network import *

router = APIRouter()

@router.get("/general")
async def main():
  status = 200
  message = "Welcome to OCS API Probe"
  data = {}
  
  try: 
    # Get CPU temperature
    CPU_TEMP = get_cpu_temperature()
    
    # Get IP addresses
    LAN_IPV4, LAN_IPV6 = get_interface_ip_addresses(os.getenv("INTERFACE_LAN"))
    WLAN_IPV4, WLAN_IPV6 = get_interface_ip_addresses(os.getenv("INTERFACE_WLAN"))
    
    # Check DNS resolver
    LAN_DNS = check_dns_resolver(os.getenv("URL_CHECK_DNS_RESOLVER"), LAN_IPV4)
    WLAN_DNS = check_dns_resolver(os.getenv("URL_CHECK_DNS_RESOLVER"), WLAN_IPV4)
        
    data = {
        "identity": os.getenv("IDENTITY"),
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
        },
        "uptime": time.time() - psutil.boot_time(),
        "location": {
          "latitude": os.getenv("LATITUDE"),
          "longitude": os.getenv("LONGITUDE"),
        },
        "network": {
          "lan":{
                "ipv4_and_ipv6": True if LAN_IPV4 is not None and LAN_IPV6 is not None else False,
                "ipv4": LAN_IPV4,
                "ipv6": LAN_IPV6,
                "dns": {
                    "status": LAN_DNS.status,
                    "hostname": LAN_DNS.hostname,
                    "ip_address": LAN_DNS.ip_address,
                    "response_time": LAN_DNS.response_time,
                }
            },
            "wlan":{
                "ipv4_and_ipv6": True if WLAN_IPV4 is not None and WLAN_IPV6 is not None else False,
                "ipv4": WLAN_IPV4,
                "ipv6": WLAN_IPV6,
                "dns": {
                    "status": WLAN_DNS.status,
                    "hostname": WLAN_DNS.hostname,
                    "ip_address": WLAN_DNS.ip_address,
                    "response_time": WLAN_DNS.response_time,
                }
            }
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
  