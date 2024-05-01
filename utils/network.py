import prometheus_client as prom
from prometheus_client import CollectorRegistry

# Network Metrics
network_registry = CollectorRegistry()

# DNS Metrics
DNS_STATUS = prom.Info("DNS_STATUS", "DNS Resovler Status", registry=network_registry)
DNS_DETAIL = prom.Info("DNS_DETAIL", "DNS Resolver Details", registry=network_registry)

# IP Metrics
IP_STATUS = prom.Info("IP_STATUS", "IP Address Status", registry=network_registry)
IP_DETAIL = prom.Info("IP_DETAIL", "IP Address Details", registry=network_registry)