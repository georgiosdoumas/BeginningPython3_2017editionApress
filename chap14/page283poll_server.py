#!/usr/bin/python3.6

import socket, select
servers_socket = socket.socket()
server_host = socket.gethostname()
port = 1234
number_of_connections = 5
try:
    servers_socket.bind((server_host, port))
    file_descriptor_map = { servers_socket.fileno(): servers_socket }
    servers_socket.listen(number_of_connections)
    p = select.poll()
    p.register(servers_socket)
    print("PollServer started, listening on port ", port)
except Exception as conerr:
    print("Could not start server due to :", conerr)
else:
    try:
        while True:
            events_tuple = p.poll()
            for fd, event in events_tuple:
                if fd in file_descriptor_map:
                    client_connection_socket, client_addr = servers_socket.accept()
                    print('Got connection from', client_addr)
                    p.register(client_connection_socket)
                    file_descriptor_map[client_connection_socket.fileno()] = client_connection_socket
                elif event & select.POLLIN:
                    data = file_descriptor_map[fd].recv(1024)
                    if not data:
                        print(file_descriptor_map[fd].getpeername(), ' disconnected')
                        p.unregister(fd)
                        del file_descriptor_map[fd]
                    else:
                        print(data)
    except Exception as pollerr:
        print(" Could not perform poll, due to ", pollerr)
    except KeyboardInterrupt:
        print("Server was stopped by a Ctrl+C. Exiting program")
