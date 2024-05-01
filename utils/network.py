import prometheus_client as prom
from prometheus_client import CollectorRegistry

# Network Metrics
network_registry = CollectorRegistry()

# DNS Metrics
DNS_STATUS = prom.Info("DNS_STATUS", "DNS Resovler Status", registry=network_registry)
DNS_RESPONSE_TIME = prom.Info("DNS_RESPONSE_TIME", "DNS Resovler Response Time", registry=network_registry)

# IP Metrics
IP_ADDRESS = prom.Info("IP_ADDRESS", "IP Address", registry=network_registry)
IP_STATUS = prom.Info("IP_STATUS", "IP Address Status", registry=network_registry)