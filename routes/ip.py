from fastapi import APIRouter
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
        IP_ADDRESS.info({
            "wlan": {
                "status": result.data.wlan.ipv4_and_ipv6,
                "ipv4": result.data.wlan.ipv4,
                "ipv6": result.data.wlan.ipv6
            },
            "lan" : {
                "status": result.data.lan.ipv4_and_ipv6,
                "ipv4": result.data.lan.ipv4,
                "ipv6": result.data.lan.ipv6
            }
        })
        
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