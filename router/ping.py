from fastapi import APIRouter
from icmplib import ping
from dotenv import load_dotenv, dotenv_values
import datetime
import psutil
import netifaces

class PingResults:
    def __init__(self, source, internal, external):
        self.source = source
        self.internal = internal
        self.external = external

def ping_by_interface(interface, env):
    try:
        source = netifaces.ifaddresses(interface)[netifaces.AF_INET][0]['addr']
        internal = ping(env["INTERNAL_GATEWAY"], count=int(env["PING_COUNT"]), source=source, interval=0.2)
        external = ping(env["EXTERNAL_GATEWAY"], count=int(env["PING_COUNT"]), source=source, interval=0.2)
        return PingResults(source, internal, external)
    except KeyError:
        raise ValueError("Unable to connect NIC, please recheck the interface name.")
    except Exception as e:
        raise ValueError(str(e))

# Load Environment
load_dotenv()
env = dotenv_values(".env")
router = APIRouter()

@router.get("/ping")
async def main():
    status = 200
    message = "Welcome to OCS API Probe"
    data = {}

    try:
        lan_ping = ping_by_interface(env["INTERFACE_LAN"], env)
        wifi_ping = ping_by_interface(env["INTERFACE_WIFI"], env)

        data = {
            "timeStamp": datetime.datetime.now(),
            "nic": list(psutil.net_if_addrs().keys()),
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
            "wifi": {
                "src": wifi_ping.source,
                "ping": {
                    "internal": {
                        "host": wifi_ping.internal.address,
                        "minRTT": wifi_ping.internal.min_rtt,
                        "maxRTT": wifi_ping.internal.max_rtt,
                        "avgRTT": wifi_ping.internal.avg_rtt,
                        "packetsSent": wifi_ping.internal.packets_sent,
                        "packetsReceived": wifi_ping.internal.packets_received,
                        "packetsLoss": wifi_ping.internal.packet_loss
                    },
                    "external": {
                        "host": wifi_ping.external.address,
                        "minRTT": wifi_ping.external.min_rtt,
                        "maxRTT": wifi_ping.external.max_rtt,
                        "avgRTT": wifi_ping.external.avg_rtt,
                        "packetsSent": wifi_ping.external.packets_sent,
                        "packetsReceived": wifi_ping.external.packets_received,
                        "packetsLoss": wifi_ping.external.packet_loss
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
