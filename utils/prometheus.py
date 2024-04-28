import prometheus_client as prom

#General Metrics
CPU_CORE = prom.Gauge("CPU_CORE", "Number of CPU Cores")
CPU_THREAD = prom.Gauge("CPU_THREAD", "Number of CPU Threads")
CPU_USAGE = prom.Gauge("CPU_USAGE", "CPU Usage")
CPU_TEMPERATURE = prom.Gauge("CPU_TEMPERATURE", "CPU Temperature")
RAM_USAGE = prom.Gauge("RAM_USAGE", "RAM Usage")
RAM_AVAILABLE = prom.Gauge("RAM_AVAILABLE", "RAM Available")
RAM_TOTAL = prom.Gauge("RAM_TOTAL", "RAM Total")
UPTIME = prom.Gauge("UPTIME", "System Uptime")
LATITUDE = prom.Info("LATITUDE", "Latitude of the Probe")
LONGITUDE = prom.Info("LONGITUDE", "Longitude of the Probe")

# DNS Metrics
DNS_STATUS = prom.Info("DNS_STATUS", "DNS Status")
DNS_HOSTNAME = prom.Info("DNS_HOSTNAME", "DNS Hostname")
DNS_IP_ADDRESS = prom.Info("DNS_IP_ADDRESS", "DNS IP Address")
DNS_RESPONSE_TIME = prom.Gauge("DNS_RESPONSE_TIME", "DNS Response Time")

# IP Metrics
## LAN
LAN_IPV4_AND_IPV6 = prom.Info("LAN_IPV4_AND_IPV6", "LAN IPv4 and IPv6 Address Status")
LAN_IPV4 = prom.Info("LAN_IPV4", "LAN IPv4 Address")
LAN_IPV6 = prom.Info("LAN_IPV6", "LAN IPv6 Address")
## WLAN
WLAN_IPV4_AND_IPV6 = prom.Info("WLAN_IPV4_AND_IPV6", "WLAN IPv4 and IPv6 Address Status")
WLAN_IPV4 = prom.Info("WLAN_IPV4", "WLAN IPv4 Address")
WLAN_IPV6 = prom.Info("WLAN_IPV6", "WLAN IPv6 Address")

# Speedtest Metrics
LAN_ST_SRC_IP = prom.Info("LAN_SRC_IP", "LAN Source IP Address")
LAN_ST_DOWNLOAD = prom.Gauge("LAN_DOWNLOAD", "LAN Download Speed")
LAN_ST_UPLOAD = prom.Gauge("LAN_UPLOAD", "LAN Upload Speed")
WLAN_ST_SRC_IP = prom.Info("WLAN_SRC_IP", "WLAN Source IP Address")
WLAN_ST_DOWNLOAD = prom.Gauge("WLAN_DOWNLOAD", "WLAN Download Speed")
WLAN_ST_UPLOAD = prom.Gauge("WLAN_UPLOAD", "WLAN Upload Speed")

# Ping Metrics
## LAN Internal
LAN_IN_PING_SRC_IP = prom.Info("LAN_IN_PING_SRC_IP", "LAN Test Internal Source IP Address")
LAN_IN_PING_DST_IP = prom.Info("LAN_IN_PING_DST_IP", "LAN Test Internal Destination IP Address")
LAN_IN_PING_MIN = prom.Gauge("LAN_IN_PING_MIN", "LAN Test Internal Minimum Ping")
LAN_IN_PING_AVG = prom.Gauge("LAN_IN_PING_AVG", "LAN Test Internal Average Ping")
LAN_IN_PING_MAX = prom.Gauge("LAN_IN_PING_MAX", "LAN Test Internal Maximum Ping")
LAN_IN_PING_PKT_SENT = prom.Gauge("LAN_IN_PING_PKT_SENT", "LAN Test Internal Packet Sent")
LAN_IN_PING_PKT_RCVD = prom.Gauge("LAN_IN_PING_PKT_RCVD", "LAN Test Internal Packet Received")
LAN_IN_PING_PKT_LOSS = prom.Gauge("LAN_IN_PING_PKT_LOSS", "LAN Test Internal Packet Loss")
## LAN External
LAN_EX_PING_SRC_IP = prom.Info("LAN_EX_PING_SRC_IP", "LAN Test External Source IP Address")
LAN_EX_PING_DST_IP = prom.Info("LAN_EX_PING_DST_IP", "LAN Test External Destination IP Address")
LAN_EX_PING_MIN = prom.Gauge("LAN_EX_PING_MIN", "LAN Test External Minimum Ping")
LAN_EX_PING_AVG = prom.Gauge("LAN_EX_PING_AVG", "LAN Test External Average Ping")
LAN_EX_PING_MAX = prom.Gauge("LAN_EX_PING_MAX", "LAN Test External Maximum Ping")
LAN_EX_PING_PKT_SENT = prom.Gauge("LAN_EX_PING_PKT_SENT", "LAN Test External Packet Sent")
LAN_EX_PING_PKT_RCVD = prom.Gauge("LAN_EX_PING_PKT_RCVD", "LAN Test External Packet Received")
LAN_EX_PING_PKT_LOSS = prom.Gauge("LAN_EX_PING_PKT_LOSS", "LAN Test External Packet Loss")
## WLAN Internal
WLAN_IN_PING_SRC_IP = prom.Info("WLAN_IN_PING_SRC_IP", "WLAN Test Internal Source IP Address")
WLAN_IN_PING_DST_IP = prom.Info("WLAN_IN_PING_DST_IP", "WLAN Test Internal Destination IP Address")
WLAN_IN_PING_MIN = prom.Gauge("WLAN_IN_PING_MIN", "WLAN Test Internal Minimum Ping")
WLAN_IN_PING_AVG = prom.Gauge("WLAN_IN_PING_AVG", "WLAN Test Internal Average Ping")
WLAN_IN_PING_MAX = prom.Gauge("WLAN_IN_PING_MAX", "WLAN Test Internal Maximum Ping")
WLAN_IN_PING_PKT_SENT = prom.Gauge("WLAN_IN_PING_PKT_SENT", "WLAN Test Internal Packet Sent")
WLAN_IN_PING_PKT_RCVD = prom.Gauge("WLAN_IN_PING_PKT_RCVD", "WLAN Test Internal Packet Received")
WLAN_IN_PING_PKT_LOSS = prom.Gauge("WLAN_IN_PING_PKT_LOSS", "WLAN Test Internal Packet Loss")
## WLAN External
WLAN_EX_PING_SRC_IP = prom.Info("WLAN_EX_PING_SRC_IP", "WLAN Test External Source IP Address")
WLAN_EX_PING_DST_IP = prom.Info("WLAN_EX_PING_DST_IP", "WLAN Test External Destination IP Address")
WLAN_EX_PING_MIN = prom.Gauge("WLAN_EX_PING_MIN", "WLAN Test External Minimum Ping")
WLAN_EX_PING_AVG = prom.Gauge("WLAN_EX_PING_AVG", "WLAN Test External Average Ping")
WLAN_EX_PING_MAX = prom.Gauge("WLAN_EX_PING_MAX", "WLAN Test External Maximum Ping")
WLAN_EX_PING_PKT_SENT = prom.Gauge("WLAN_EX_PING_PKT_SENT", "WLAN Test External Packet Sent")
WLAN_EX_PING_PKT_RCVD = prom.Gauge("WLAN_EX_PING_PKT_RCVD", "WLAN Test External Packet Received")
WLAN_EX_PING_PKT_LOSS = prom.Gauge("WLAN_EX_PING_PKT_LOSS", "WLAN Test External Packet Loss")