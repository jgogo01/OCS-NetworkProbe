from fastapi import APIRouter, Response
from prometheus_client import generate_latest
import requests
from schemas.ip import IPResult
from utils.prometheus import *
    
router = APIRouter()
@router.get("/metrics/ip")
async def metrics(target: str):
    try:
        request = requests.get(f"http://{target}:4000/ip").json()
        result = IPResult(request["status"], request["message"], request["data"])
        
        #Set Prometheus metrics
        LAN_IPV4_AND_IPV6.info(result.data.lan.ipv4_and_ipv6)
        LAN_IPV4.info(result.data.lan.ipv4)
        LAN_IPV6.info(result.data.lan.ipv6)
        WLAN_IPV4_AND_IPV6.info(result.data.wlan.ipv4_and_ipv6)
        WLAN_IPV4.info(result.data.wlan.ipv4)
        WLAN_IPV6.info(result.data.wlan.ipv6)
        
        return {
            "status": 200,
            "message": "Updated Prometheus metrics",
            "data": {}
        }
    except Exception as e:
        return {
            "status": 500,
            "message": str(e),
            "data": {}
        }