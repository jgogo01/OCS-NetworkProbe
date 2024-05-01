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
        checkStatus = network.data.lan.dns.status and network.data.wlan.dns.status and network.data.lan.ipv4_and_ipv6 and network.data.wlan.ipv4_and_ipv6
        
        GEO_MAP.info({
            "indentity": general.data.identity,
            "latitude": general.data.location.latitude,
            "longitude": general.data.location.longitude,
            "overall_status": "True" if checkStatus else "False",
            "lan_dns": "True" if network.data.lan.dns.status == True else "False",
            "wlan_dns": "True" if network.data.wlan.dns.status == True else "False",
            "lan_ipv4_and_ipv6": "True" if network.data.lan.ipv4_and_ipv6 == True else "False",
            "wlan_ipv4_and_ipv6": "True" if network.data.wlan.ipv4_and_ipv6 == True else "False"
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