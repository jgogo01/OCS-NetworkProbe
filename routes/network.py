import requests
from schemas.general import GeneralResult
from schemas.network import NetworkResult
from fastapi import APIRouter, Response
from prometheus_client import generate_latest
from utils.network import *

router = APIRouter()

@router.get("/metrics/network/")
async def metrics(target: str):
    try:
        #Get network
        requestNetwork = requests.get(f"http://{target}/network").json()
        requestGeneral = requests.get(f"http://{target}/general").json()
        network = NetworkResult(requestNetwork["status"], requestNetwork["message"], requestNetwork["data"])
        general = GeneralResult(requestGeneral["status"], requestGeneral["message"], requestGeneral["data"])
        
        #Set Prometheus metrics
        ## DNS
        DNS_STATUS.info({
            "indentity": general.data.identity,
            "dns_status": "True" if network.data.lan.dns.status and
            network.data.wlan.dns.status else "False",
            "lan_dns": "True" if network.data.lan.dns.status else "False",
            "wlan_dns": "True" if network.data.wlan.dns.status else "False",
            "lan_dns_response_time": f"{network.data.lan.dns.response_time}",
            "wlan_dns_response_time": f"{network.data.wlan.dns.response_time}"
        })

        ## IP
        IP_STATUS.info({
            "lan_ipv4": network.data.lan.ipv4 if network.data.lan.ipv4 != None else "",
            "lan_ipv6": network.data.lan.ipv6 if network.data.lan.ipv6 != None else "",
            "wlan_ipv4": network.data.wlan.ipv4 if network.data.wlan.ipv4 != None else "",
            "wlan_ipv6": network.data.wlan.ipv6 if network.data.wlan.ipv6 != None else "",
            "lan_ipv4": "1" if network.data.lan.ipv4 != None else "0",
            "lan_ipv6": "1" if network.data.lan.ipv6 != None else "0",
            "wlan_ipv4": "1" if network.data.wlan.ipv4 != None else "0",
            "wlan_ipv6": "1" if network.data.wlan.ipv6 != None else "0",
            "lan_ipv4_and_ipv6": "1" if network.data.lan.ipv4_and_ipv6 else "0",
            "wlan_ipv4_and_ipv6": "1" if network.data.wlan.ipv4_and_ipv6 else "0",
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