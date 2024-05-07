from fastapi import APIRouter
from icmplib import ping
import datetime
import netifaces
import os
from dotenv import load_dotenv

load_dotenv()

class PingResults:
    def __init__(self, source, internal, external):
        self.source = source
        self.internal = internal
        self.external = external

def ping_by_interface(interface):
    try:
        source = netifaces.ifaddresses(interface)[netifaces.AF_INET][0]['addr']
        internal = ping(os.getenv("INTERNAL_GATEWAY"), count=int(os.getenv("PING_COUNT")), source=source, interval=0.2)
        external = ping(os.getenv("EXTERNAL_GATEWAY"), count=int(os.getenv("PING_COUNT")), source=source, interval=0.2)
        return PingResults(source, internal, external)
    except KeyError:
        raise ValueError("Unable to connect NIC, please recheck the interface name.")
    except Exception as e:
        raise ValueError(str(e))

router = APIRouter()

@router.get("/ping")
async def main():
    status = 200
    message = "Welcome to OCS API Probe"
    data = {}

    try:
        lan_ping = ping_by_interface(os.getenv("INTERFACE_LAN"))
    except Exception as e:
        lan_ping = None
    
    try:
        wlan_ping = ping_by_interface(os.getenv("INTERFACE_WLAN"))
    except Exception as e:
        wlan_ping = None
    
    data = {
            "timeStamp": datetime.datetime.now(),
            "lan": {
                "src": lan_ping.source if lan_ping != None else None,
                "ping": {
                    "internal": {
                        "dst": lan_ping.internal.address if lan_ping != None else None,
                        "minRTT": lan_ping.internal.min_rtt if lan_ping != None else 0,
                        "maxRTT": lan_ping.internal.max_rtt if lan_ping != None else 0,
                        "avgRTT": lan_ping.internal.avg_rtt if lan_ping != None else 0,
                        "packetsSent": lan_ping.internal.packets_sent if lan_ping != None else 0,
                        "packetsReceived": lan_ping.internal.packets_received if lan_ping != None else 0,
                        "packetsLoss": lan_ping.internal.packet_loss if lan_ping != None else 0
                    },
                    "external": {
                        "dst": lan_ping.external.address if lan_ping != None else None,
                        "minRTT": lan_ping.external.min_rtt if lan_ping != None else 0,
                        "maxRTT": lan_ping.external.max_rtt if lan_ping != None else 0,
                        "avgRTT": lan_ping.external.avg_rtt if lan_ping != None else 0,
                        "packetsSent": lan_ping.external.packets_sent if lan_ping != None else 0,
                        "packetsReceived": lan_ping.external.packets_received if lan_ping != None else 0,
                        "packetsLoss": lan_ping.external.packet_loss if lan_ping != None else 0
                    }
                }
            },
            "wlan": {
                "src": wlan_ping.source if wlan_ping != None else None,
                "ping": {
                    "internal": {
                        "dst": wlan_ping.internal.address if wlan_ping != None else None,
                        "minRTT": wlan_ping.internal.min_rtt if wlan_ping != None else 0,
                        "maxRTT": wlan_ping.internal.max_rtt if wlan_ping != None else 0,
                        "avgRTT": wlan_ping.internal.avg_rtt if wlan_ping != None else 0,
                        "packetsSent": wlan_ping.internal.packets_sent if wlan_ping != None else 0,
                        "packetsReceived": wlan_ping.internal.packets_received if wlan_ping != None else 0,
                        "packetsLoss": wlan_ping.internal.packet_loss if wlan_ping != None else 0
                    },
                    "external": {
                        "dst": wlan_ping.external.address if wlan_ping != None else 0,
                        "minRTT": wlan_ping.external.min_rtt if wlan_ping != None else 0,
                        "maxRTT": wlan_ping.external.max_rtt if wlan_ping != None else 0,
                        "avgRTT": wlan_ping.external.avg_rtt if wlan_ping != None else 0,
                        "packetsSent": wlan_ping.external.packets_sent if wlan_ping != None else 0,
                        "packetsReceived": wlan_ping.external.packets_received if wlan_ping != None else 0,
                        "packetsLoss": wlan_ping.external.packet_loss if wlan_ping != None else 0
                    }
                }
            }
        }

    return {
        "status": status,
        "message": message,
        "data": data
    }
