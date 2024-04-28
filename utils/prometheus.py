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
LOCATION = prom.Info("LOCATION", "Location Information")

# DNS Metrics
DNS_STATUS = prom.Gauge("DNS_STATUS", "DNS Resovler Status")
DNS_RESPONSE_TIME = prom.Gauge("DNS_RESPONSE_TIME", "DNS Response Time")
DNS_DETAIL = prom.Info("DNS_DETAIL", "DNS Details")

# IP Metrics
LAN_IPV4_AND_IPV6_STATUS = prom.Gauge("LAN_IPV4_AND_IPV6_STATUS", "LAN IPv4 and IPv6 Status")
LAN_IP_ADDRESS = prom.Info("LAN_IP_ADDRESS", "LAN IP Address")
WLAN_IPV4_AND_IPV6_STATUS = prom.Gauge("WLAN_IPV4_AND_IPV6_STATUS", "WLAN IPv4 and IPv6 Status")
WLAN_IP_ADDRESS = prom.Info("WLAN_IP_ADDRESS", "WLAN IP Address")

# Speedtest Metrics
LAN_ST_DOWNLOAD = prom.Gauge("LAN_DOWNLOAD", "LAN Download Speed")
LAN_ST_UPLOAD = prom.Gauge("LAN_UPLOAD", "LAN Upload Speed")
WLAN_ST_DOWNLOAD = prom.Gauge("WLAN_DOWNLOAD", "WLAN Download Speed")
WLAN_ST_UPLOAD = prom.Gauge("WLAN_UPLOAD", "WLAN Upload Speed")

# Ping Metrics
## LAN Internal
LAN_PING_DST = prom.Info("LAN_PING_DST", "LAN Test Internal Destination")
LAN_IN_PING_MIN = prom.Gauge("LAN_IN_PING_MIN", "LAN Test Internal Minimum Ping")
LAN_IN_PING_AVG = prom.Gauge("LAN_IN_PING_AVG", "LAN Test Internal Average Ping")
LAN_IN_PING_MAX = prom.Gauge("LAN_IN_PING_MAX", "LAN Test Internal Maximum Ping")
LAN_IN_PING_PKT_SENT = prom.Gauge("LAN_IN_PING_PKT_SENT", "LAN Test Internal Packet Sent")
LAN_IN_PING_PKT_RCVD = prom.Gauge("LAN_IN_PING_PKT_RCVD", "LAN Test Internal Packet Received")
LAN_IN_PING_PKT_LOSS = prom.Gauge("LAN_IN_PING_PKT_LOSS", "LAN Test Internal Packet Loss")
## LAN External
LAN_EX_PING_MIN = prom.Gauge("LAN_EX_PING_MIN", "LAN Test External Minimum Ping")
LAN_EX_PING_AVG = prom.Gauge("LAN_EX_PING_AVG", "LAN Test External Average Ping")
LAN_EX_PING_MAX = prom.Gauge("LAN_EX_PING_MAX", "LAN Test External Maximum Ping")
LAN_EX_PING_PKT_SENT = prom.Gauge("LAN_EX_PING_PKT_SENT", "LAN Test External Packet Sent")
LAN_EX_PING_PKT_RCVD = prom.Gauge("LAN_EX_PING_PKT_RCVD", "LAN Test External Packet Received")
LAN_EX_PING_PKT_LOSS = prom.Gauge("LAN_EX_PING_PKT_LOSS", "LAN Test External Packet Loss")
## WLAN Internal
WLAN_PING_DST = prom.Info("WLAN_PING_DST", "WLAN Test Internal Destination") 
WLAN_IN_PING_MIN = prom.Gauge("WLAN_IN_PING_MIN", "WLAN Test Internal Minimum Ping")
WLAN_IN_PING_AVG = prom.Gauge("WLAN_IN_PING_AVG", "WLAN Test Internal Average Ping")
WLAN_IN_PING_MAX = prom.Gauge("WLAN_IN_PING_MAX", "WLAN Test Internal Maximum Ping")
WLAN_IN_PING_PKT_SENT = prom.Gauge("WLAN_IN_PING_PKT_SENT", "WLAN Test Internal Packet Sent")
WLAN_IN_PING_PKT_RCVD = prom.Gauge("WLAN_IN_PING_PKT_RCVD", "WLAN Test Internal Packet Received")
WLAN_IN_PING_PKT_LOSS = prom.Gauge("WLAN_IN_PING_PKT_LOSS", "WLAN Test Internal Packet Loss")
## WLAN External
WLAN_EX_PING_MIN = prom.Gauge("WLAN_EX_PING_MIN", "WLAN Test External Minimum Ping")
WLAN_EX_PING_AVG = prom.Gauge("WLAN_EX_PING_AVG", "WLAN Test External Average Ping")
WLAN_EX_PING_MAX = prom.Gauge("WLAN_EX_PING_MAX", "WLAN Test External Maximum Ping")
WLAN_EX_PING_PKT_SENT = prom.Gauge("WLAN_EX_PING_PKT_SENT", "WLAN Test External Packet Sent")
WLAN_EX_PING_PKT_RCVD = prom.Gauge("WLAN_EX_PING_PKT_RCVD", "WLAN Test External Packet Received")
WLAN_EX_PING_PKT_LOSS = prom.Gauge("WLAN_EX_PING_PKT_LOSS", "WLAN Test External Packet Loss")