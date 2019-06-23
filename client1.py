import socket

import threading  

hote = "localhost"
port = 15555

class THE(threading.Thread):
    def __init__(self,socket):
        threading.Thread.__init__(self)
        self.conn= socket

    def run(self):
        qit=0
        while True:
            print("Entrez votre message")
            data=input()
            if "exit" in data:
                qit=1
            data = data.encode("utf8")
            socket.sendall(data)
            if qit==1:
                print ("Déconnecté!")
                socket.close()
                break


class THR(threading.Thread):
    def __init__(self,socket):
        threading.Thread.__init__(self)
        self.conn= socket

    def run(self):
        while True:
            from_server=socket.recv(255)
            from_server= from_server.decode("utf8")
            print(from_server)


socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((hote, port))
print ("Connecté sur le port {}".format(port))

emission=THE(socket)
reception=THR(socket)

emission.start()
reception.start()


emission.join()
reception.join()





