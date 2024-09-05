import iperf3

server = iperf3.Server()
server.bind_address = '0.0.0.0'
server.port = 4000
server.verbose = False

print("Iperf3 Server is running at 4000")
while True:
    server.run()