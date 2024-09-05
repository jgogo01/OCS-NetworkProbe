import requests
from schemas.general import GeneralResult
from fastapi import APIRouter, Response
from prometheus_client import generate_latest
from utils.general import *
from requests.adapters import HTTPAdapter

router = APIRouter()

session = requests.Session()
adapter = HTTPAdapter(max_retries=10)
session.mount('http://', adapter)
session.mount('https://', adapter)

@router.get("/metrics/general/")
async def metrics(target: str):
    try:
        general = session.get(f"http://{target}/general").json()
        result = GeneralResult(general["status"], general["message"], general["data"])
        
        #Set Prometheus metrics
        ## General
        CPU_CORE.set(result.data.system.cpu.core)
        CPU_THREAD.set(result.data.system.cpu.thread)
        CPU_USAGE.set(result.data.system.cpu.usage)
        CPU_TEMPERATURE.set(result.data.system.cpu.temperature)
        RAM_USAGE.set(result.data.system.ram.usage)
        RAM_AVAILABLE.set(result.data.system.ram.available)
        RAM_TOTAL.set(result.data.system.ram.total)
        UPTIME.set(result.data.uptime)
        IDENTITY.info({"identity": result.data.identity})
        
        ## DNS
        DNS_STATUS.info({
            result.data.identity: "True" if result.data.network.lan.dns.status and
                                result.data.network.wlan.dns.status else "False",
        })
        DNS_DETAIL.info({
            "identity": result.data.identity,
            "lan_dns": result.data.network.lan.dns.ip_address if result.data.network.lan.dns.ip_address != None else "",
            "wlan_dns": result.data.network.wlan.dns.ip_address if result.data.network.wlan.dns.ip_address != None else "",
            "lan_dns_response_time": f"{result.data.network.lan.dns.response_time}",
            "wlan_dns_response_time": f"{result.data.network.wlan.dns.response_time}"
        })

        ## IP
        IP_STATUS.info({
            result.data.identity: "True" if result.data.network.lan.ipv4_and_ipv6 and result.data.network.wlan.ipv4_and_ipv6 else "False"
        })
        IP_DETAIL.info({
                "lan_ipv4": result.data.network.lan.ipv4 if result.data.network.lan.ipv4 != None else "",
                "lan_ipv6": result.data.network.lan.ipv6 if result.data.network.lan.ipv6 != None else "",
                "wlan_ipv4": result.data.network.wlan.ipv4 if result.data.network.wlan.ipv4 != None else "",
                "wlan_ipv6": result.data.network.wlan.ipv6 if result.data.network.wlan.ipv6 != None else ""
        })
        
        checkStatus = result.data.network.lan.dns.status and result.data.network.wlan.dns.status and result.data.network.lan.ipv4_and_ipv6 and result.data.network.wlan.ipv4_and_ipv6
        ## Map
        GEO_MAP.info({
            "identity": result.data.identity,
            "latitude": result.data.location.latitude,
            "longitude": result.data.location.longitude,
            "overall_status": "True" if checkStatus else "False",
            "lan_dns": "True" if result.data.network.lan.dns.status == True else "False",
            "wlan_dns": "True" if result.data.network.wlan.dns.status == True else "False",
            "lan_ipv4_and_ipv6": "True" if result.data.network.lan.ipv4_and_ipv6 == True else "False",
            "wlan_ipv4_and_ipv6": "True" if result.data.network.wlan.ipv4_and_ipv6 == True else "False"
        })
        
        return Response(
        media_type="text/plain",
        content=generate_latest(registry=general_registry)
        )
    except Exception as e:
        return {
            "status": 500,
            "message": str(e),
            "data": {}
        }