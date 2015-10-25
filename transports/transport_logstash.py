import socket
import json
import sys

from transports import MonyTransport

class MonyLogstash(MonyTransport):
    def __init__(self):
        MonyTransport.__init__(self)

    def createConnexion(self):
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        except socket.error, msg:
            sys.stderr.write("[ERROR1-] %s\n" % msg[1])
            sys.exit(1)

        try:
            self.sock.connect((self.host, self.port))
        except socket.error, msg:
            sys.stderr.write("[ERROR] %s\n" % msg[1])
            sys.exit(2)

    def send(self, msg):
        self.createConnexion()
        self.sock.send(json.dumps(msg))
        self.sock.close()
