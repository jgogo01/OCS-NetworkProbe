import requests
from schemas.dns import DNSResult
from fastapi import APIRouter
from utils.prometheus import *

router = APIRouter()

@router.get("/metrics/dns/")
async def metrics(target: str):
    try:
        general = requests.get(f"http://{target}/dns").json()
        result = DNSResult(general["status"], general["message"], general["data"])
        
        #Set Prometheus metrics
        DNS_STATUS.info({
            "status": result.status,
            "hostname": result.data.hostname,
            "ip_address": result.data.ip_address,
            "response_time": result.data.response_time
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