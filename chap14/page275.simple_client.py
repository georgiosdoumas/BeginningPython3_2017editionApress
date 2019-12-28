#!/usr/bin/python3.6

import socket

client_socket = socket.socket()
server_host = socket.gethostname() # here the server is the same PC as the client
# 
port_to_connect_on_server = 1234
receiving_packets_size = 1024
try:
    client_socket.connect((server_host, port_to_connect_on_server))
    print(client_socket.recv(receiving_packets_size))
except Exception as er:
    print("Failed to retreive info due to error:", er)
