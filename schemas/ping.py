class Ping:
    def __init__(self, dst, minRTT, maxRTT, avgRTT, packetsSent, packetsReceived, packetsLoss):
        self.dst = dst
        self.minRTT = minRTT
        self.maxRTT = maxRTT
        self.avgRTT = avgRTT
        self.packetsSent = packetsSent
        self.packetsReceived = packetsReceived
        self.packetsLoss = packetsLoss

class Interface:
    def __init__(self, src, internal_ping, external_ping):
        self.src = src
        self.internal_ping = internal_ping
        self.external_ping = external_ping

class PingData:
    def __init__(self, lan, wifi):
        self.lan = lan
        self.wifi = wifi

class PingResult:
    def __init__(self, status, message, data):
        self.status = status
        self.message = message
        self.data = PingData(
            lan=Interface(
                src=data["lan"]["src"],
                internal_ping=Ping(**data["lan"]["ping"]["internal"]),
                external_ping=Ping(**data["lan"]["ping"]["external"])
            ),
            wifi=Interface(
                src=data["wifi"]["src"],
                internal_ping=Ping(**data["wifi"]["ping"]["internal"]),
                external_ping=Ping(**data["wifi"]["ping"]["external"])
            )
        )
