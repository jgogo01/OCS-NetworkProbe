import netifaces
from fastapi import APIRouter
import os

def get_interface_ip_addresses(interface):
    try:
        addrs = netifaces.ifaddresses(interface)
        ipv4_address = addrs.get(netifaces.AF_INET, [])
        ipv4_address = ipv4_address[0]['addr'] if ipv4_address else None

        ipv6_address = None
        ipv6_addrs = addrs.get(netifaces.AF_INET6, [])
        for addr in ipv6_addrs:
            if addr['addr'].startswith('fe80:'):
                continue  # Skip link-local addresses
            ipv6_address = addr['addr']
            break

        return ipv4_address, ipv6_address
    except (KeyError, IndexError):
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
                "ipv4_and_ipv6": True if LAN_IPV4 is not None and LAN_IPV6 is not None else False,
                "ipv4": LAN_IPV4,
                "ipv6": LAN_IPV6,
                "dns": LAN_DNS
            },
            "wifi":{
                "ipv4_and_ipv6": True if WIFI_IPV4 is not None and WIFI_IPV6 is not None else False,
                "ipv4": WIFI_IPV4,
                "ipv6": WIFI_IPV6,
                "dns": WIFI_DNS
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
