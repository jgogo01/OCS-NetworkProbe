import netifaces
from fastapi import APIRouter
import os
import socket
import time

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

def check_dns_resolution(hostname, interface=None):
    try:
        start_time = time.time()
        
        # Create a socket and bind it to the specified interface if provided
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if interface:
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_BINDTODEVICE, bytes(interface, "utf-8"))
        
        # Resolve DNS
        ip_address = socket.gethostbyname(hostname)

        end_time = time.time()
        response_time = end_time - start_time
        return DNS(True, hostname, ip_address, response_time)
    except socket.gaierror:
        return DNS(False, hostname, None, None)

router = APIRouter()

@router.get("/network")
async def main():
    status = 200
    message = "Welcome to OCS API Probe"
    data = {}
    
    try:
        LAN_IPV4, LAN_IPV6 = get_interface_ip_addresses(os.getenv("INTERFACE_LAN"))
        WLAN_IPV4, WLAN_IPV6 = get_interface_ip_addresses(os.getenv("INTERFACE_WLAN"))
        LAN_DNS = check_dns_resolution(os.getenv("URL_CHECK_DNS_RESOLVER"), os.getenv("INTERFACE_LAN"))
        WIFI_DNS = check_dns_resolution(os.getenv("URL_CHECK_DNS_RESOLVER"), os.getenv("INTERFACE_WLAN"))
        
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
                    "status": WIFI_DNS.status,
                    "hostname": WIFI_DNS.hostname,
                    "ip_address": WIFI_DNS.ip_address,
                    "response_time": WIFI_DNS.response_time,
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
