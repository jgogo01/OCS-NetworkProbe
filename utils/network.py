import prometheus_client as prom
from prometheus_client import CollectorRegistry

# Network Metrics
network_registry = CollectorRegistry()

# DNS Metrics
DNS_STATUS = prom.Info("DNS_STATUS", "DNS Resovler Status")
DNS_RESPONSE_TIME = prom.Info("DNS_RESPONSE_TIME", "DNS Resovler Response Time")

# IP Metrics
IP_ADDRESS = prom.Info("IP_ADDRESS", "IP Address")
IP_STATUS = prom.Info("IP_STATUS", "IP Address Status")