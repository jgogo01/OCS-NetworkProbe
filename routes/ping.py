import requests
from schemas.ping import PingResult
from fastapi import APIRouter, Response
from utils.prometheus import *
from prometheus_client import generate_latest

router = APIRouter()

@router.get("/metrics/ping/")
async def metrics(target: str):
    try:
        ping = requests.get(f"http://{target}/ping").json()
        result = PingResult(ping["status"], ping["message"], ping["data"])
        
        #Set Prometheus metrics
        LAN_PING_DST.info({
                "internal": result.data.lan.internal_ping.dst,
                "external": result.data.lan.external_ping.dst
        })
        LAN_IN_PING_MIN.set(result.data.lan.internal_ping.minRTT)
        LAN_IN_PING_MAX.set(result.data.lan.internal_ping.maxRTT)
        LAN_IN_PING_AVG.set(result.data.lan.internal_ping.avgRTT)
        LAN_IN_PING_PKT_SENT.set(result.data.lan.internal_ping.packetsSent)
        LAN_IN_PING_PKT_RCVD.set(result.data.lan.internal_ping.packetsReceived)
        LAN_IN_PING_PKT_LOSS.set(result.data.lan.internal_ping.packetsLoss)
        LAN_EX_PING_MIN.set(result.data.lan.external_ping.minRTT)
        LAN_EX_PING_MAX.set(result.data.lan.external_ping.maxRTT)
        LAN_EX_PING_AVG.set(result.data.lan.external_ping.avgRTT)
        LAN_EX_PING_PKT_SENT.set(result.data.lan.external_ping.packetsSent)
        LAN_EX_PING_PKT_RCVD.set(result.data.lan.external_ping.packetsReceived)
        LAN_EX_PING_PKT_LOSS.set(result.data.lan.external_ping.packetsLoss)
        
        WLAN_PING_DST.info({
                "internal": result.data.wlan.internal_ping.dst,
                "external": result.data.wlan.external_ping.dst
        })
        WLAN_IN_PING_MIN.set(result.data.wlan.internal_ping.minRTT)
        WLAN_IN_PING_MAX.set(result.data.wlan.internal_ping.maxRTT)
        WLAN_IN_PING_AVG.set(result.data.wlan.internal_ping.avgRTT)
        WLAN_IN_PING_PKT_SENT.set(result.data.wlan.internal_ping.packetsSent)
        WLAN_IN_PING_PKT_RCVD.set(result.data.wlan.internal_ping.packetsReceived)
        WLAN_IN_PING_PKT_LOSS.set(result.data.wlan.internal_ping.packetsLoss)
        WLAN_EX_PING_MIN.set(result.data.wlan.external_ping.minRTT)
        WLAN_EX_PING_MAX.set(result.data.wlan.external_ping.maxRTT)
        WLAN_EX_PING_AVG.set(result.data.wlan.external_ping.avgRTT)
        WLAN_EX_PING_PKT_SENT.set(result.data.wlan.external_ping.packetsSent)
        WLAN_EX_PING_PKT_RCVD.set(result.data.wlan.external_ping.packetsReceived)
        WLAN_EX_PING_PKT_LOSS.set(result.data.wlan.external_ping.packetsLoss)
        
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