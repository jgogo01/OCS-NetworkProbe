import netifaces
from fastapi import APIRouter
import os
import socket
import time
import dns.resolver
import platform

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

class DNS:
    def __init__(self, status, hostname, ip_address, response_time):
        self.status = status
        self.hostname = hostname
        self.ip_address = ip_address
        self.response_time = response_time

def check_dns_resolver(hostname, src_address):
    if src_address is None:
        return DNS(False, None, None, None)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind((src_address, 0))
        s.settimeout(10)
        
        start_time = time.time()  # Record start time
        ip = socket.gethostbyname(hostname)
        end_time = time.time()    # Record end time
        response_time = end_time - start_time  # Calculate response time
        
        return DNS(True, hostname, ip, response_time)
    except socket.error as e:
        print("Unable to resolve hostname", str(e))
        return DNS(False, None, None, None)
    finally:
        s.close()

router = APIRouter()

@router.get("/network")
async def main():
    status = 200
    message = "Welcome to OCS API Probe"
    data = {}
    
    try:
        LAN_IPV4, LAN_IPV6 = get_interface_ip_addresses(os.getenv("INTERFACE_LAN"))
        WLAN_IPV4, WLAN_IPV6 = get_interface_ip_addresses(os.getenv("INTERFACE_WLAN"))
        LAN_DNS = check_dns_resolver(os.getenv("URL_CHECK_DNS_RESOLVER"), LAN_IPV4)
        WLAN_DNS = check_dns_resolver(os.getenv("URL_CHECK_DNS_RESOLVER"), WLAN_IPV4)
        
        data = {
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
    except Exception as e:
        status = 500
        message = str(e)
        
    return {
        "status": status,
        "message": message,
        "data": data
    }
