import prometheus_client as prom
from prometheus_client import CollectorRegistry

geo_registry = CollectorRegistry()
# Geo Metrics
GEO_MAP = prom.Info("GEO_MAP", "Geo Map", registry=geo_registry)