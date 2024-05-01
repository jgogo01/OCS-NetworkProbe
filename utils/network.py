import prometheus_client as prom
from prometheus_client import CollectorRegistry

# Network Metrics
network_registry = CollectorRegistry()

# DNS Metrics
DNS_STATUS = prom.Gauge("DNS_STATUS", "DNS Resovler Status")
LAN_DNS_STATUS = prom.Gauge("LAN_DNS_STATUS", "LAN DNS Status")
WLAN_DNS_STATUS = prom.Gauge("WLAN_DNS_STATUS", "WLAN DNS Status")
LAN_DNS_RESPONSE_TIME = prom.Gauge("LAN_DNS_RESPONSE_TIME", "LAN DNS Response Time")
WLAN_DNS_RESPONSE_TIME = prom.Gauge("WLAN_DNS_RESPONSE_TIME", "WLAN DNS Response Time")

# IP Metrics
IP_ADDRESS = prom.Info("IP_ADDRESS", "IP Address")
LAN_IPV4_AND_IPV6_STATUS = prom.Gauge("LAN_IPV4_AND_IPV6_STATUS", "LAN IPv4 and IPv6 Status")
WLAN_IPV4_AND_IPV6_STATUS = prom.Gauge("WLAN_IPV4_AND_IPV6_STATUS", "WLAN IPv4 and IPv6 Status")