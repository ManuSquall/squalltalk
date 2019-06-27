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
            #///////
            if(self.cpt==0):
                T.append(client)
                self.cpt=1

            #affichage clients
            # client.sendall(chaine_vide)
            # client.sendall(chaine_vide)
            # text="Le client " + str(address) + " vient de se connecter!"
            # text=text.encode("utf8")
            # client.sendall(text)
            # client.sendall(chaine_vide)
            # client.sendall(chaine_vide)

            #affichage serveur
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
                            #print("message envoyé au client: ", text)
                        #/////////////////////////
                        # Affichage au niveau de chaque machine
                        # text="client "+ str(address)+message
                        # text=text.encode("utf8")
                        # if(T!=""):
                        #     with threading.RLock():
                        #         T=text
                        #client.sendall(text)
                        #////////////////////////
                    else:
                        #affichage serveur
                        print()
                        print()
                        print("Le client {} s'est déconnecté".format( address ))
                        #print(T)
                        for i in T:
                            if(i==client):
                                del T[T.index(client)]
                        client.close()
                        print()
                        print()

                        #affichage clients
                        # client.sendall(chaine_vide)
                        # client.sendall(chaine_vide)
                        # text="Le client " + str(address) + " s'est déconnecté!"
                        # text=text.encode("utf8")
                        # client.sendall(text)
                        # client.sendall(chaine_vide)
                        # client.sendall(chaine_vide)
                        break

# class THE(threading.Thread):
#     def __init__(self, socket1, socket2, socket3):
#         threading.Thread.__init__(self)
#         self.con1= socket1
#         self.con2= socket2
#         self.con3= socket3

#     def run(self):
#         global T
#         while True:
#             if(T!=""):
#                 self.con1.
                


socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(('', 15555))


# while True:
#     THR(socket).start()
#     THR(socket).join()


th1=THR(socket)
th2=THR(socket)
th3=THR(socket)
th4=THR(socket)


th1.start()
th2.start()
th3.start()
th4.start()


th1.join()                    
th2.join()                    
th3.join()                    
th4.join()                    

print ("Close")
socket.close()

