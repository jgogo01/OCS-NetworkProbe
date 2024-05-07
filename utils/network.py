import socket
import time
import netifaces

class DNS:
    def __init__(self, status, hostname, ip_address, response_time):
        self.status = status
        self.hostname = hostname
        self.ip_address = ip_address
        self.response_time = response_time

def get_interface_ip_addresses(interface):
    try:
        addrs = netifaces.ifaddresses(interface)
        ipv4_address = addrs.get(netifaces.AF_INET, [])
        ipv4_address = ipv4_address[0]['addr'] if ipv4_address else None

        ipv6_address = None
        ipv6_addrs = addrs.get(netifaces.AF_INET6, [])
        for addr in ipv6_addrs:
            if addr['addr'].startswith('fe80:'):
                continue  # Skip link-local addresses
            ipv6_address = addr['addr']
            break

        return ipv4_address, ipv6_address
    except (KeyError, IndexError):
        return None, None
    
def check_dns_resolver(hostname, src_address):
    if src_address is None:
        return DNS(False, None, None, None)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind((src_address, 0))
        s.settimeout(10)
        
        start_time = time.time()  # Record start time
        ip = socket.gethostbyname(hostname)
        end_time = time.time()    # Record end time
        response_time = end_time - start_time  # Calculate response time
        
        return DNS(True, hostname, ip, response_time)
    except socket.error as e:
        print("Unable to resolve hostname", str(e))
        return DNS(False, None, None, None)
    finally:
        s.close()