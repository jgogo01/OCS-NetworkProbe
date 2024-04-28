class DNSResult:
    def __init__(self, status, message, data):
        self.status = status
        self.message = message
        self.data = Data(**data)
        
class Data:
    def __init__(self, status, hostname, ip_address, response_time):
        self.status = status
        self.hostname = hostname
        self.ip_address = ip_address
        self.response_time = response_time