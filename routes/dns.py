import requests
from schemas.dns import DNSResult
from fastapi import APIRouter, Response
from prometheus_client import generate_latest
from utils.prometheus import *

router = APIRouter()

@router.get("/metrics/dns/")
async def metrics(target: str):
    try:
        general = requests.get("http://{target}:4000/general").json()
        result = DNSResult(general["status"], general["message"], general["data"])
        
        #Set Prometheus metrics
        DNS_HOSTNAME.info(result.data.hostname)
        DNS_IP_ADDRESS.info(result.data.ip_address)
        DNS_RESPONSE_TIME.set(result.data.response_time)
        DNS_STATUS.info(result.status)
        
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