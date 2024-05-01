import requests
from schemas.general import GeneralResult
from schemas.network import NetworkResult
from fastapi import APIRouter, Response
from prometheus_client import generate_latest
from utils.map import *

router = APIRouter()

@router.get("/metrics/map/")
async def metrics(target: str):
    try:
        #Get latitute and longitude
        requestGeneral = requests.get(f"http://{target}/general").json()
        requestNetwork = requests.get(f"http://{target}/network").json()
        
        #Schema
        general = GeneralResult(requestGeneral["status"], requestGeneral["message"], requestGeneral["data"])
        network = NetworkResult(requestNetwork["status"], requestNetwork["message"], requestNetwork["data"])
        
        GEO_MAP.info({
            "indentity": general.data.identity,
            "latitude": general.data.location.latitude,
            "longitude": general.data.location.longitude,
            "lan_dns": 1 if network.data.lan.dns.status == True else 0,
            "wlan_dns": 1 if network.data.wlan.dns.status == True else 0,
            "lan_ipv4_and_ipv6": 1 if network.data.lan.ipv4_and_ipv6 == True else 0,
            "wlan_ipv4_and_ipv6": 1 if network.data.wlan.ipv4_and_ipv6 == True else 0
            })

        return Response(
        media_type="text/plain",
        content=generate_latest(registry=geo_registry)
        )
    except Exception as e:
        return {
            "status": 500,
            "message": str(e),
            "data": {}
        }