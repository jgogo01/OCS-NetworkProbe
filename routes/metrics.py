import requests
from fastapi import APIRouter, Response
from prometheus_client import generate_latest
from utils.prometheus import *
# Import the schemas
from schemas.speedtest import SpeedtestResult
from schemas.ping import PingResult
    
router = APIRouter()
@router.get("/metrics")
async def metrics():
    return Response(
        media_type="text/plain",
        content=generate_latest()
        )

@router.get("/metrics/speedtest/")
async def metrics(target: str):
    speedtest = requests.get(f"http://{target}/speedtest").json()
    result = SpeedtestResult(speedtest["status"], speedtest["message"], speedtest["data"])
    
    #Set Prometheus metrics
    LAN_ST_SRC_IP.info({"src": result.data.lan.src})
    LAN_ST_DOWNLOAD.set(result.data.lan.speedtest.download)
    LAN_ST_UPLOAD.set(result.data.lan.speedtest.upload)
    WIFI_ST_SRC_IP.info({"src": result.data.wifi.src})
    WIFI_ST_DOWNLOAD.set(result.data.wifi.speedtest.download)
    WIFI_ST_UPLOAD.set(result.data.wifi.speedtest.upload)

    return Response(
        media_type="text/plain",
        content=generate_latest()
        )
    
@router.get("/metrics/ping/")
async def metrics(target: str):
    ping = requests.get(f"http://{target}/ping").json()
    result = PingResult(ping["status"], ping["message"], ping["data"])
    
    print(result.data.lan.internal_ping)
    
    #Set Prometheus metrics
    LAN_IN_PING_SRC_IP.info({"src": result.data.lan.src})
    LAN_IN_PING_MIN.set(result.data.lan.internal_ping.minRTT)
    LAN_IN_PING_MAX.set(result.data.lan.internal_ping.maxRTT)
    LAN_IN_PING_AVG.set(result.data.lan.internal_ping.avgRTT)
    LAN_IN_PING_PKT_SENT.set(result.data.lan.internal_ping.packetsSent)
    LAN_IN_PING_PKT_RCVD.set(result.data.lan.internal_ping.packetsReceived)
    LAN_IN_PING_PKT_LOSS.set(result.data.lan.internal_ping.packetsLoss)
    LAN_EX_PING_SRC_IP.info({"src": result.data.lan.src})
    LAN_EX_PING_MIN.set(result.data.lan.external_ping.minRTT)
    LAN_EX_PING_MAX.set(result.data.lan.external_ping.maxRTT)
    LAN_EX_PING_AVG.set(result.data.lan.external_ping.avgRTT)
    LAN_EX_PING_PKT_SENT.set(result.data.lan.external_ping.packetsSent)
    LAN_EX_PING_PKT_RCVD.set(result.data.lan.external_ping.packetsReceived)
    LAN_EX_PING_PKT_LOSS.set(result.data.lan.external_ping.packetsLoss)
    WIFI_IN_PING_SRC_IP.info({"src": result.data.wifi.src})
    WIFI_IN_PING_MIN.set(result.data.wifi.internal_ping.minRTT)
    WIFI_IN_PING_MAX.set(result.data.wifi.internal_ping.maxRTT)
    WIFI_IN_PING_AVG.set(result.data.wifi.internal_ping.avgRTT)
    WIFI_IN_PING_PKT_SENT.set(result.data.wifi.internal_ping.packetsSent)
    WIFI_IN_PING_PKT_RCVD.set(result.data.wifi.internal_ping.packetsReceived)
    WIFI_IN_PING_PKT_LOSS.set(result.data.wifi.internal_ping.packetsLoss)
    WIFI_EX_PING_SRC_IP.info({"src": result.data.wifi.src})
    WIFI_EX_PING_MIN.set(result.data.wifi.external_ping.minRTT)
    WIFI_EX_PING_MAX.set(result.data.wifi.external_ping.maxRTT)
    WIFI_EX_PING_AVG.set(result.data.wifi.external_ping.avgRTT)
    WIFI_EX_PING_PKT_SENT.set(result.data.wifi.external_ping.packetsSent)
    WIFI_EX_PING_PKT_RCVD.set(result.data.wifi.external_ping.packetsReceived)
    WIFI_EX_PING_PKT_LOSS.set(result.data.wifi.external_ping.packetsLoss)
    
    return Response(
        media_type="text/plain",
        content=generate_latest()
        )