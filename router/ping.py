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
        wlan_ping = ping_by_interface(os.getenv("INTERFACE_WLAN"))

        data = {
            "timeStamp": datetime.datetime.now(),
            "lan": {
                "src": lan_ping.source,
                "ping": {
                    "internal": {
                        "dst": lan_ping.internal.address,
                        "minRTT": lan_ping.internal.min_rtt,
                        "maxRTT": lan_ping.internal.max_rtt,
                        "avgRTT": lan_ping.internal.avg_rtt,
                        "packetsSent": lan_ping.internal.packets_sent,
                        "packetsReceived": lan_ping.internal.packets_received,
                        "packetsLoss": lan_ping.internal.packet_loss
                    },
                    "external": {
                        "dst": lan_ping.external.address,
                        "minRTT": lan_ping.external.min_rtt,
                        "maxRTT": lan_ping.external.max_rtt,
                        "avgRTT": lan_ping.external.avg_rtt,
                        "packetsSent": lan_ping.external.packets_sent,
                        "packetsReceived": lan_ping.external.packets_received,
                        "packetsLoss": lan_ping.external.packet_loss
                    }
                }
            },
            "wlan": {
                "src": wlan_ping.source,
                "ping": {
                    "internal": {
                        "dst": wlan_ping.internal.address,
                        "minRTT": wlan_ping.internal.min_rtt,
                        "maxRTT": wlan_ping.internal.max_rtt,
                        "avgRTT": wlan_ping.internal.avg_rtt,
                        "packetsSent": wlan_ping.internal.packets_sent,
                        "packetsReceived": wlan_ping.internal.packets_received,
                        "packetsLoss": wlan_ping.internal.packet_loss
                    },
                    "external": {
                        "dst": wlan_ping.external.address,
                        "minRTT": wlan_ping.external.min_rtt,
                        "maxRTT": wlan_ping.external.max_rtt,
                        "avgRTT": wlan_ping.external.avg_rtt,
                        "packetsSent": wlan_ping.external.packets_sent,
                        "packetsReceived": wlan_ping.external.packets_received,
                        "packetsLoss": wlan_ping.external.packet_loss
                    }
                }
            }
        }
    except Exception as e:
        status = 500
        message = str(e)

    return {
        "status": status,
        "message": message,
        "data": data
    }
