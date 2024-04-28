class DNSResult:
    def __init__(self, status :int, message :str, data :dict):
        self.status = status
        self.message = message
        self.data = Data(**data)
        
class Data:
    def __init__(self, status :int, hostname :str, ip_address :str, response_time :float):
        self.status = status
        self.hostname = hostname
        self.ip_address = ip_address
        self.response_time = response_time