import prometheus_client as prom
from prometheus_client import CollectorRegistry

# Network Metrics
network_registry = CollectorRegistry()

# DNS Metrics
DNS_STATUS = prom.Info("DNS_STATUS", "DNS Resovler Status", registry=network_registry)

# IP Metrics
IP_ADDRESS = prom.Info("IP_ADDRESS", "IP Address", registry=network_registry)