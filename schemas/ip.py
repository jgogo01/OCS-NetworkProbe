class IPResult:
    def __init__(self, status :int, message :str, data :dict):
        self.status = status
        self.message = message
        self.data = Data(**data)
        
class Data:
    def __init__(self, lan: dict, wlan: dict):
        self.lan = IP(**lan)
        self.wlan = IP(**wlan)
        
class IP:
    def __init__(self, ipv4_and_ipv6 :bool, ipv4 :str, ipv6 :str):
        self.ipv4_and_ipv6 = ipv4_and_ipv6
        self.ipv4 = ipv4
        self.ipv6 = ipv6