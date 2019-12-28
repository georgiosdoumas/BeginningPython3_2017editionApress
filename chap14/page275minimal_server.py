#!/usr/bin/python3.6
# A better implementation of the example from the book. Better names, and some error handling
import socket, time

server_socket = socket.socket()
server_host = socket.gethostname()  # If you do not want to use 127.0.0.1 , then put here the IP of the interface that will serve
msg = 'Thank you for connecting, and bye'
bytes_to_send = msg.encode()
server_listening_port = 1234   ## try putting port 22 here to get an error!
number_of_connections = 2

try:
    server_socket.bind((server_host, server_listening_port))
    server_socket.listen(number_of_connections)
    print("Server is running, listening  on port:", server_listening_port, " for a maximum of ", number_of_connections, "incoming connections.\n Stop it with Ctrl+C!")
except Exception as er:
    print("Could not start server due to :", er)
    
else:
    try:
        while True:
            client_con , client_addr = server_socket.accept()
            print("Accpeted a connection from:", client_addr)
            time.sleep(5)
            client_con.send(bytes_to_send)
            client_con.close()
    except (KeyboardInterrupt, Exception) as er :
        print("Server was stopped (maybe by a Ctrl+C). Exiting program", er)
        
