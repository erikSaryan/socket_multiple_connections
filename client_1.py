import socket

class Client():
    def __init__(self):
        self.host = socket.gethostname()
        self.port = 8001
        self.BUFFER_SIZE = 1024
        self.tcpClientA = self.create_socket()

    def create_socket(self):
        tcpClientA = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcpClientA.connect((self.host, self.port))
        return tcpClientA

    def send_meesage(self):
        message = ""
        while (message != 'exit'):
            message = input("Enter message  --> ")
            self.tcpClientA.send(message.encode())
            data = self.tcpClientA.recv(self.BUFFER_SIZE).decode()
            print("Client_A received data:", data)
        self.tcpClientA.close()

client_A = Client()
client_A.send_meesage()


