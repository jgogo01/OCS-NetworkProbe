import prometheus_client as prom
from prometheus_client import CollectorRegistry

# Ping Metrics
ping_registry = CollectorRegistry()
## LAN Internal
LAN_PING_DST = prom.Info("LAN_PING_DST", "LAN Test Internal Destination", registry=ping_registry)
LAN_IN_PING_MIN = prom.Gauge("LAN_IN_PING_MIN", "LAN Test Internal Minimum Ping", registry=ping_registry)
LAN_IN_PING_AVG = prom.Gauge("LAN_IN_PING_AVG", "LAN Test Internal Average Ping", registry=ping_registry)
LAN_IN_PING_MAX = prom.Gauge("LAN_IN_PING_MAX", "LAN Test Internal Maximum Ping", registry=ping_registry)
LAN_IN_PING_PKT_SENT = prom.Gauge("LAN_IN_PING_PKT_SENT", "LAN Test Internal Packet Sent", registry=ping_registry)
LAN_IN_PING_PKT_RCVD = prom.Gauge("LAN_IN_PING_PKT_RCVD", "LAN Test Internal Packet Received", registry=ping_registry)
LAN_IN_PING_PKT_LOSS = prom.Gauge("LAN_IN_PING_PKT_LOSS", "LAN Test Internal Packet Loss", registry=ping_registry)
## LAN External
LAN_EX_PING_MIN = prom.Gauge("LAN_EX_PING_MIN", "LAN Test External Minimum Ping", registry=ping_registry)
LAN_EX_PING_AVG = prom.Gauge("LAN_EX_PING_AVG", "LAN Test External Average Ping", registry=ping_registry)
LAN_EX_PING_MAX = prom.Gauge("LAN_EX_PING_MAX", "LAN Test External Maximum Ping", registry=ping_registry)
LAN_EX_PING_PKT_SENT = prom.Gauge("LAN_EX_PING_PKT_SENT", "LAN Test External Packet Sent", registry=ping_registry)
LAN_EX_PING_PKT_RCVD = prom.Gauge("LAN_EX_PING_PKT_RCVD", "LAN Test External Packet Received", registry=ping_registry)
LAN_EX_PING_PKT_LOSS = prom.Gauge("LAN_EX_PING_PKT_LOSS", "LAN Test External Packet Loss", registry=ping_registry)
## WLAN Internal
WLAN_PING_DST = prom.Info("WLAN_PING_DST", "WLAN Test Internal Destination", registry=ping_registry) 
WLAN_IN_PING_MIN = prom.Gauge("WLAN_IN_PING_MIN", "WLAN Test Internal Minimum Ping", registry=ping_registry)
WLAN_IN_PING_AVG = prom.Gauge("WLAN_IN_PING_AVG", "WLAN Test Internal Average Ping", registry=ping_registry)
WLAN_IN_PING_MAX = prom.Gauge("WLAN_IN_PING_MAX", "WLAN Test Internal Maximum Ping", registry=ping_registry)
WLAN_IN_PING_PKT_SENT = prom.Gauge("WLAN_IN_PING_PKT_SENT", "WLAN Test Internal Packet Sent", registry=ping_registry)
WLAN_IN_PING_PKT_RCVD = prom.Gauge("WLAN_IN_PING_PKT_RCVD", "WLAN Test Internal Packet Received", registry=ping_registry)
WLAN_IN_PING_PKT_LOSS = prom.Gauge("WLAN_IN_PING_PKT_LOSS", "WLAN Test Internal Packet Loss", registry=ping_registry)
## WLAN External
WLAN_EX_PING_MIN = prom.Gauge("WLAN_EX_PING_MIN", "WLAN Test External Minimum Ping", registry=ping_registry)
WLAN_EX_PING_AVG = prom.Gauge("WLAN_EX_PING_AVG", "WLAN Test External Average Ping", registry=ping_registry)
WLAN_EX_PING_MAX = prom.Gauge("WLAN_EX_PING_MAX", "WLAN Test External Maximum Ping", registry=ping_registry)
WLAN_EX_PING_PKT_SENT = prom.Gauge("WLAN_EX_PING_PKT_SENT", "WLAN Test External Packet Sent", registry=ping_registry)
WLAN_EX_PING_PKT_RCVD = prom.Gauge("WLAN_EX_PING_PKT_RCVD", "WLAN Test External Packet Received", registry=ping_registry)
WLAN_EX_PING_PKT_LOSS = prom.Gauge("WLAN_EX_PING_PKT_LOSS", "WLAN Test External Packet Loss", registry=ping_registry)