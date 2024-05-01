import requests
from schemas.general import GeneralResult
from schemas.network import NetworkResult
from fastapi import APIRouter, Response
from prometheus_client import generate_latest
from utils.network import *

router = APIRouter()

@router.get("/metrics/map/")
async def metrics(target: str):
    try:
        #Get network
        requestNetwork = requests.get(f"http://{target}/network").json()
        network = NetworkResult(requestNetwork["status"], requestNetwork["message"], requestNetwork["data"])
        
        #Set Prometheus metrics
        ## DNS
        DNS_STATUS.set({
            1 if network.data.lan.dns.status and
                 network.data.wlan.dns.status else 0
        })
        LAN_DNS_STATUS.set({
            1 if network.data.lan.dns.status else 0
        })
        WLAN_DNS_STATUS.set({
            1 if network.data.wlan.dns.status else 0
        })
        LAN_DNS_RESPONSE_TIME.set({
            network.data.lan.dns.response_time
        })
        WLAN_DNS_RESPONSE_TIME.set({
            network.data.wlan.dns.response_time
        })
        
        ## IP
        IP_ADDRESS.info({
            "lan_ipv4": network.data.lan.ipv4,
            "lan_ipv6": network.data.lan.ipv6,
            "wlan_ipv4": network.data.wlan.ipv4,
            "wlan_ipv6": network.data.wlan.ipv6
        })
        LAN_IPV4_AND_IPV6_STATUS.set({
            1 if network.data.lan.ipv4 and
                 network.data.lan.ipv6 else 0
        })
        WLAN_IPV4_AND_IPV6_STATUS.set({
            1 if network.data.wlan.ipv4 and
                 network.data.wlan.ipv6 else 0
        })

        return Response(
        media_type="text/plain",
        content=generate_latest(registry=network_registry)
        )
    except Exception as e:
        return {
            "status": 500,
            "message": str(e),
            "data": {}
        }