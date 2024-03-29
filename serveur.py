import socket

import threading

T=[]

#affichage à envoyer aux clients
chaine_vide=" "
chaine_vide=chaine_vide.encode("utf8")

#   thread de reception pour recevoir les messages des clients
#  recevoir les messages des clients!
class THR(threading.Thread):
    def __init__(self, socket):
        threading.Thread.__init__(self)
        self.conn=socket
        self.cpt=0

    def run(self):
        global T
        while True:     
            socket.listen(5)
            client, address = socket.accept()
            if(self.cpt==0):
                T.append(client)
                self.cpt=1

            #affichage lorsqu'une connexion est établie
            print()
            print()
            print ("Le client {} vient de se  connecter".format( address ))
            print()
            print()


            while True:
                message = client.recv(255)
                if message:
                    message = message.decode("utf8")
                    if message!="exit":
                        print ("client {}: ".format(address),message)
                        for i in T:
                            text="client "+ str(address)+message
                            text=text.encode("utf8")
                            i.sendall(text)
                    else:
                        #affichage serveur
                        print()
                        print()
                        print("Le client {} s'est déconnecté".format( address ))
                        for i in T:
                            if(i==client):
                                del T[T.index(client)]
                        client.close()
                        print()
                        print()
                        break
                


socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(('', 15555))

print("==================================================:")
print("\nServeur démarré et à l'écoute de connexion cliente:\n")
print("==================================================:")


 # initialisation des threads
th1=THR(socket)
th2=THR(socket)
th3=THR(socket)
th4=THR(socket)

# demarrage des threads
th1.start()
th2.start()
th3.start()
th4.start()

# connexion
th1.join()                    
th2.join()                    
th3.join()                    
th4.join()                    

print ("Close")
socket.close()

