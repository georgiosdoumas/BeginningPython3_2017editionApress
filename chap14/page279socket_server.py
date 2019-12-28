#!/usr/bin/python3.6
# Simple implementation based on the book Listing 14.3

from socketserver import TCPServer, StreamRequestHandler

class ClientHandler(StreamRequestHandler):
    def handle(self):
        addr = self.request.getpeername()
        msg_to_client = 'Thank you for connecting to basic SocketServer'
        print('Got connection from', addr)
        self.wfile.write(bytes(msg_to_client, 'utf-8'))

listening_port = 1234        
try:
    socket_server = TCPServer(('', listening_port), ClientHandler)
    print("Simple socketServer started, listening on port ",listening_port)
    print("...[stop by Ctrl+C]")
    socket_server.serve_forever()
except Exception as setuper:
    print(" Could not start server, due to :", setuper)
except KeyboardInterrupt:
    print("Server was stopped by a Ctrl+C. Exiting program")
