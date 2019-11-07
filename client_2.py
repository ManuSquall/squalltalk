import tkinter
import socket
import threading 

global s
s=0
global data
data=""



# ////////////////////////////////////////////////////////////////////////////////////////////////////////////


#                                          ///////////////////////////////////////
#                                                           SQUALL  
#                                          ///////////////////////////////////////








# ////////////////////////////////////////////////////////////////////////////////////////////////////////////


# ////////////////////////////////////////////////////////////////////////////////////////////////////////////



#                                          ///////////////////////////////////////
#                                                    SOCKET ET THREADING
#                                          ///////////////////////////////////////

 

hote = "localhost"
port = 15555
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

class THE(threading.Thread):
    def __init__(self,socket):
        threading.Thread.__init__(self)
        self.conn= socket

    def run(self):
        
        data = "client connecté"
        data = data.encode("utf8")
        socket.sendall(data)


class THR(threading.Thread):
    def __init__(self,socket):
        threading.Thread.__init__(self)
        self.conn= socket

    def run(self):
        while True:
            from_server=socket.recv(255)
            print(from_server)
            from_server= from_server.decode("utf8")
            #print(from_server)
            listbox.insert(tkinter.END ,from_server+"\n")

socket.connect((hote, port))
print ("Connecté sur le port {}".format(port))

emission=THE(socket)
reception=THR(socket)

def squall():
    
    emission.start()
    reception.start()


    



# ////////////////////////////////////////////////////////////////////////////////////////////////////////////





# ////////////////////////////////////////////////////////////////////////////////////////////////////////////



#                                          ///////////////////////////////////////
#                                                        TKINTER
#                                          ///////////////////////////////////////



# barre de scroll
from tkinter import ttk

#instance de la fenetre principale
fenetre = tkinter.Tk()


def envoyer(event):
    #on prend le contenu du input tkinter, on le sauvegarde puis le retourne
    # à data
    # data=(message.get()+"\n")
    # message.delete(0, tkinter.END)
    # s=1
    qit=0
    data=message.get()+"\n"
    if "exit" in data:
        qit=1
    if data!="":
        data = data.encode("utf8")
        socket.sendall(data)
    if qit==1:
        print ("Déconnecté!")
        socket.close()
    message.delete(0, tkinter.END)

def deconnecter(event):
    emission.join()
    reception.join()
    



#couleur d'arrière plan
bgcolor="#4065A4"

#personalisation design fenetre
fenetre.title("SquallTalk V1")
fenetre.maxsize(500,500)
fenetre.minsize(500,500)
fenetre.iconbitmap("squall.ico")
fenetre.config(background=bgcolor)



#declaration des frames
main_frame = tkinter.Frame(fenetre, bg=bgcolor)

frame1 = tkinter.Frame(main_frame, bg=bgcolor)
frame2 = tkinter.Frame(main_frame, bg=bgcolor)
frame3 = tkinter.Frame(main_frame, bg=bgcolor)

#widgets?
titre = tkinter.Label(
                frame1, 
                text="SquallTalk V1", 
                font=("arial", 30),
                bg=bgcolor,
                fg="#ffffff"
            )
#titre.pack()
titre.grid(row=0, column=2, sticky=tkinter.W)


scroll = tkinter.Scrollbar(frame2)
scroll.pack(side=tkinter.RIGHT, fill=tkinter.Y)
listbox = tkinter.Listbox(frame2, width=70, yscrollcommand=scroll.set)

listbox.pack(side=tkinter.LEFT)
scroll.config(command=listbox.yview)



#boutons
btn1 = tkinter.Button(frame3, text="Se connecter",font=("arial", 10), command=squall)
# btn1.pack()
btn1.grid(row=0, column=0, sticky=tkinter.W)


message = tkinter.Entry(
                frame3, 
                bd=5, 
                font=("arial", 10),
                bg=bgcolor,
                fg="#ffffff",
                relief=tkinter.RIDGE,
                width=50
                )
# message.pack()
message.grid(row=1, column=0, sticky=tkinter.W)

btn2 = tkinter.Button(frame3, text="Envoyer",font=("arial", 10))
btn2.grid(row=1, column=1, sticky=tkinter.W)
btn2.bind("<Button-1>", envoyer)

btn3 = tkinter.Button(frame3, text="Se deconnecter",font=("arial", 10))
btn3.grid(row=1, column=3, sticky=tkinter.W)
btn3.bind("<Button-1>", deconnecter)

frame1.pack(expand=tkinter.YES)
frame2.pack()
frame3.pack(expand=tkinter.YES)

main_frame.pack()

fenetre.bind()

#boucle principale d'affichage de la fenetre
fenetre.mainloop()


# ////////////////////////////////////////////////////////////////////////////////////////////////////////////


