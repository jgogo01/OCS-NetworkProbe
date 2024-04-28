import socket
import time
import os

from fastapi import APIRouter
router = APIRouter()

def check_dns_resolution(hostname):
    try:
        start_time = time.time()
        ip_address = socket.gethostbyname(hostname)

        end_time = time.time()
        response_time = end_time - start_time
        return True, hostname, ip_address, response_time
    except socket.gaierror:
        return False, hostname, None, None


@router.get("/dns")
async def main():    
    status = 200
    message = "Welcome to OCS API Probe"
    data = {}
    
    try: 
        ckStatus, hostname, ip_address, response_time = check_dns_resolution(os.getenv("URL_CHECK_DNS_RESOLVER")) 
        data = {
            "status": ckStatus,
            "hostname": hostname,
            "ip_address": ip_address,
            "response_time": response_time,
        }
    except Exception as e:
        status = 500
        message = str(e)
        data = {} 
  
    return {
        "status": status,
        "message": message,
        "data": data
    }