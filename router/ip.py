import netifaces
from fastapi import APIRouter
import os

def get_interface_ip_addresses(interface):
  try:
    addrs = netifaces.ifaddresses(interface)
    ipv4_address = addrs.get(netifaces.AF_INET, []).get('addr')
    ipv6_address = None
    ipv6_addrs = addrs.get(netifaces.AF_INET6, [])
    for addr in ipv6_addrs:
      if not netifaces.is_link_local(addr['addr']):
        ipv6_address = addr['addr']
        break
    return ipv4_address, ipv6_address
  except (netifaces.exceptions.IFAddressesError, ValueError):
    return None, None

router = APIRouter()

@router.get("/ip")
async def main():
    status = 200
    message = "Welcome to OCS API Probe"
    data = {}
    
    try:
        LAN_IPV4, LAN_IPV6 = get_interface_ip_addresses(os.getenv("INTERFACE_LAN"))
        WIFI_IPV4, WIFI_IPV6 = get_interface_ip_addresses(os.getenv("INTERFACE_WIFI"))
        
        data = {
            "lan":{
                "ipv4": LAN_IPV4,
                "ipv6": LAN_IPV6
            },
            "wifi":{
                "ipv4": WIFI_IPV4,
                "ipv6": WIFI_IPV6
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
