import socket

class Client():
    def __init__(self):
        self.host = socket.gethostname()
        self.port = 8001
        self.BUFFER_SIZE = 1024
        self.tcpClientB = self.create_socket()

    def create_socket(self):
        tcpClientB = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcpClientB.connect((self.host, self.port))
        return tcpClientB

    def send_meesage(self):
        message = ""
        while (message != 'exit'):
            message = input("Enter message  --> ")
            self.tcpClientB.send(message.encode())
            data = self.tcpClientB.recv(self.BUFFER_SIZE).decode()
            print("Client_B received data:", data)
        self.tcpClientB.close()

client_b = Client()
client_b.send_meesage()


