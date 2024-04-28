import requests
from schemas.dns import DNSResult
from fastapi import APIRouter, Response
from prometheus_client import generate_latest
from utils.prometheus import *

router = APIRouter()

@router.get("/metrics/dns/")
async def metrics(target: str):
    try:
        general = requests.get(f"http://{target}/dns").json()
        result = DNSResult(general["status"], general["message"], general["data"])
        
        #Set Prometheus metrics
        DNS_STATUS.set(1 if result.data.status == True else 0)
        DNS_DETAIL.info({
            "hostname": result.data.hostname,
            "ip_address": result.data.ip_address,
        })
        DNS_RESPONSE_TIME.set(result.data.response_time)
        
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