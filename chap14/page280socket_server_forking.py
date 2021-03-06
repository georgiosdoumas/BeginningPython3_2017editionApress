#!/usr/bin/python3.6

from socketserver import TCPServer, StreamRequestHandler, ForkingMixIn

class forkingServer(ForkingMixIn, TCPServer):
    pass

class ClientHandler(StreamRequestHandler):
    def handle(self):
        addr = self.request.getpeername()
        msg_to_client = 'Thank you for connecting to forking SocketServer'
        print('Got connection from', addr)
        self.wfile.write(bytes(msg_to_client, 'utf-8'))

listening_port = 1234        
try:
    socket_server = forkingServer(('', listening_port), ClientHandler)
    print("Forking socketServer started, listening on port ",listening_port)
    print("...[stop by Ctrl+C]")
    socket_server.serve_forever()
except Exception as setuper:
    print(" Could not start forking server, due to :", setuper)
except KeyboardInterrupt:
    print("Server was stopped by a Ctrl+C. Exiting program")
    socket_server.server_close()  
    socket_server.shutdown()     # maybe both?
