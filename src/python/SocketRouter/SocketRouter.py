from websockets.sync.client import connect
from socket import socket
import threading

class SocketRouter:
    def __init__(self):
        self.url = "wss://discord.gg/?v=10&encoding=json"
    
    def listen(self):
        if self.ws:
            self.ws = connect(self.url)
        message = self.ws.recv()
        return message

    def send(self, message:str):
        self.ws.send(message)

class NetworkRouter:
    def __init__(self):
        self.host = "localhost"
        self.port = 20090
    
    def server_thread(self):
        sock_serv = socket.socket((socket.AP_INET, socket.SOCK_STREAM))
        sock_serv.bind((self.host, self.port))
        # while True:
            # thread = threading.Thread(target=)