#!/usr/bin/python3.6

from socketserver import TCPServer, ThreadingMixIn, StreamRequestHandler

class threadingServer(ThreadingMixIn, TCPServer):
    pass

class ClientHandler(StreamRequestHandler):
    def handle(self):
        addr = self.request.getpeername()
        msg_to_client = 'Thank you for connecting to threading SocketServer'
        print('Got connection from', addr)
        self.wfile.write(bytes(msg_to_client, 'utf-8'))

listening_port = 1234        
try:
    socket_server = threadingServer(('', listening_port), ClientHandler)
    print("Threading socketServer started, listening on port ",listening_port)
    print("...[stop by Ctrl+C]")
    socket_server.serve_forever()
except Exception as setuperr:
    print(" Could not start server, due to :", setuperr)
except KeyboardInterrupt:
    print("Server was stopped by a Ctrl+C. Exiting program")
    socket_server.server_close()  
    socket_server.shutdown()  
