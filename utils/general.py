import prometheus_client as prom
from prometheus_client import CollectorRegistry

#General Metrics
general_registry = CollectorRegistry()
INDENTITY = prom.Info("INDENTITY", "System Identity", registry=general_registry)
CPU_CORE = prom.Gauge("CPU_CORE", "Number of CPU Cores", registry=general_registry)
CPU_THREAD = prom.Gauge("CPU_THREAD", "Number of CPU Threads", registry=general_registry)
CPU_USAGE = prom.Gauge("CPU_USAGE", "CPU Usage", registry=general_registry)
CPU_TEMPERATURE = prom.Gauge("CPU_TEMPERATURE", "CPU Temperature", registry=general_registry)
RAM_USAGE = prom.Gauge("RAM_USAGE", "RAM Usage", registry=general_registry)
RAM_AVAILABLE = prom.Gauge("RAM_AVAILABLE", "RAM Available", registry=general_registry)
RAM_TOTAL = prom.Gauge("RAM_TOTAL", "RAM Total", registry=general_registry)
UPTIME = prom.Gauge("UPTIME", "System Uptime", registry=general_registry)