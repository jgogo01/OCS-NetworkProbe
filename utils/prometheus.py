import prometheus_client as prom

# Speedtest Metrics
LAN_ST_SRC_IP = prom.Info("LAN_SRC_IP", "LAN Source IP Address")
LAN_ST_DOWNLOAD = prom.Gauge("LAN_DOWNLOAD", "LAN Download Speed")
LAN_ST_UPLOAD = prom.Gauge("LAN_UPLOAD", "LAN Upload Speed")
WIFI_ST_SRC_IP = prom.Info("WIFI_SRC_IP", "WIFI Source IP Address")
WIFI_ST_DOWNLOAD = prom.Gauge("WIFI_DOWNLOAD", "WIFI Download Speed")
WIFI_ST_UPLOAD = prom.Gauge("WIFI_UPLOAD", "WIFI Upload Speed")

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
## WIFI Internal
WIFI_IN_PING_SRC_IP = prom.Info("WIFI_IN_PING_SRC_IP", "WIFI Test Internal Source IP Address")
WIFI_IN_PING_DST_IP = prom.Info("WIFI_IN_PING_DST_IP", "WIFI Test Internal Destination IP Address")
WIFI_IN_PING_MIN = prom.Gauge("WIFI_IN_PING_MIN", "WIFI Test Internal Minimum Ping")
WIFI_IN_PING_AVG = prom.Gauge("WIFI_IN_PING_AVG", "WIFI Test Internal Average Ping")
WIFI_IN_PING_MAX = prom.Gauge("WIFI_IN_PING_MAX", "WIFI Test Internal Maximum Ping")
WIFI_IN_PING_PKT_SENT = prom.Gauge("WIFI_IN_PING_PKT_SENT", "WIFI Test Internal Packet Sent")
WIFI_IN_PING_PKT_RCVD = prom.Gauge("WIFI_IN_PING_PKT_RCVD", "WIFI Test Internal Packet Received")
WIFI_IN_PING_PKT_LOSS = prom.Gauge("WIFI_IN_PING_PKT_LOSS", "WIFI Test Internal Packet Loss")
## WIFI External
WIFI_EX_PING_SRC_IP = prom.Info("WIFI_EX_PING_SRC_IP", "WIFI Test External Source IP Address")
WIFI_EX_PING_DST_IP = prom.Info("WIFI_EX_PING_DST_IP", "WIFI Test External Destination IP Address")
WIFI_EX_PING_MIN = prom.Gauge("WIFI_EX_PING_MIN", "WIFI Test External Minimum Ping")
WIFI_EX_PING_AVG = prom.Gauge("WIFI_EX_PING_AVG", "WIFI Test External Average Ping")
WIFI_EX_PING_MAX = prom.Gauge("WIFI_EX_PING_MAX", "WIFI Test External Maximum Ping")
WIFI_EX_PING_PKT_SENT = prom.Gauge("WIFI_EX_PING_PKT_SENT", "WIFI Test External Packet Sent")
WIFI_EX_PING_PKT_RCVD = prom.Gauge("WIFI_EX_PING_PKT_RCVD", "WIFI Test External Packet Received")
WIFI_EX_PING_PKT_LOSS = prom.Gauge("WIFI_EX_PING_PKT_LOSS", "WIFI Test External Packet Loss")