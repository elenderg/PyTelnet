#made by Silvan Kohler
import socket
import sys
class telnet():
    def __init__(self, ip, port):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = (ip, port)
    def connect(self):
        self.client.connect(self.server)
    def send(self, cmd, form="UTF-8"):
        self.client.send(bytes(cmd, form))
    def recieve(self, bytess):
        return str(self.client.recv(bytess), 'UTF-8')