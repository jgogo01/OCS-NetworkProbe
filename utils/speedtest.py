import prometheus_client as prom
from prometheus_client import CollectorRegistry

speedtest_registry = CollectorRegistry()

# Speedtest Metrics
LAN_ST_DOWNLOAD = prom.Gauge("LAN_DOWNLOAD", "LAN Download Speed", registry=speedtest_registry)
LAN_ST_UPLOAD = prom.Gauge("LAN_UPLOAD", "LAN Upload Speed", registry=speedtest_registry)
WLAN_ST_DOWNLOAD = prom.Gauge("WLAN_DOWNLOAD", "WLAN Download Speed", registry=speedtest_registry)
WLAN_ST_UPLOAD = prom.Gauge("WLAN_UPLOAD", "WLAN Upload Speed", registry=speedtest_registry)