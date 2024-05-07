import requests
from schemas.general import GeneralResult
from fastapi import APIRouter, Response
from prometheus_client import generate_latest
from utils.map import *

router = APIRouter()

@router.get("/metrics/map/")
async def metrics(target: str):
    try:
        #Get latitute and longitude
        request = requests.get(f"http://{target}/general").json()
        
        #Schema
        general = GeneralResult(request["status"], request["message"], request["data"])
        checkStatus = general.data.network.lan.dns.status and general.data.network.wlan.dns.status and general.data.network.lan.ipv4_and_ipv6 and general.data.network.wlan.ipv4_and_ipv6
        
        GEO_MAP.info({
            "identity": general.data.identity,
            "latitude": general.data.location.latitude,
            "longitude": general.data.location.longitude,
            "overall_status": "True" if checkStatus else "False",
            "lan_dns": "True" if general.data.network.lan.dns.status == True else "False",
            "wlan_dns": "True" if general.data.network.wlan.dns.status == True else "False",
            "lan_ipv4_and_ipv6": "True" if general.data.network.lan.ipv4_and_ipv6 == True else "False",
            "wlan_ipv4_and_ipv6": "True" if general.data.network.wlan.ipv4_and_ipv6 == True else "False"
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