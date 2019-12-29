#!/usr/bin/python3.6

import socket, select
servers_socket = socket.socket()
server_host = socket.gethostname()
port = 1234
number_of_connections = 5
try:
    servers_socket.bind((server_host, port))
    servers_socket.listen(number_of_connections)
    inputs = [servers_socket]
    print("SelectServer started, listening on port ", port)
except Exception as conerr:
    print("Could not start server due to :", conerr)
else:
    try:
        while True:
            read_list_socket, write_list_socket, exceptional_condition_socket = select.select(inputs, [], [])
            for r in read_list_socket:
                if r is servers_socket:
                    client_connection_socket, client_addr = servers_socket.accept()
                    print('Got connection from', client_addr)
                    inputs.append(client_connection_socket)
                else:
                    try:
                        data = r.recv(1024)
                        disconnected = not data
                    except socket.error:
                        disconnected = True

                    if disconnected:
                        print(r.getpeername(), 'disconnected')
                        inputs.remove(r)
                    else:
                        print(data)
    except Exception as selecterr:
        print(" Could not perform selection, due to ", selecterr)
    except KeyboardInterrupt:
        print("Server was stopped by a Ctrl+C. Exiting program")
