from fastapi import APIRouter, Response
from prometheus_client import generate_latest
import requests
from schemas.ip import IPResult
from utils.prometheus import *
    
router = APIRouter()
@router.get("/metrics/ip")
async def metrics(target: str):
    try:
        request = requests.get(f"http://{target}/ip").json()
        result = IPResult(request["status"], request["message"], request["data"])
        
        #Set Prometheus metrics
        LAN_IPV4_AND_IPV6_STATUS.set({"status": 1 if result.data.lan.status == True else 0})
        LAN_IP_ADDRESS.info({
                "ipv4": result.data.lan.ipv4,
                "ipv6": result.data.lan.ipv6 if result.data.lan.ipv6 != None else "N/A"
        })
        WLAN_IPV4_AND_IPV6_STATUS.set({"status": 1 if result.data.wlan.status == True else 0})
        WLAN_IP_ADDRESS.info({
                "ipv4": result.data.wlan.ipv4,
                "ipv6": result.data.wlan.ipv6 if result.data.wlan.ipv6 != None else "N/A"
        })
        
        return Response(
        media_type="text/plain",
        content=generate_latest()
        )
    except Exception as e:
        return {
            "status": 500,
            "message": str(e),
            "data": {}
        }