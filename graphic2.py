import tkinter

# barre de scroll
from tkinter import ttk

#instance de la fenetre principale
fenetre = tkinter.Tk()


def envoyer():
    # messchat.set(messchat.get()+ "\n" +message.get()+"\n")
    listbox.insert(tkinter.END, (messchat.get()+ "\n" +message.get()+"\n"))
    message.delete(0, tkinter.END)









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

#la variable dynamique qui s'affichera sur le chat
messchat = tkinter.StringVar()
messchat.set("   ")

# /////////////////////////////////////////////////////////////////////////

# chat = tkinter.Label(
#                 frame2, 
#                 # text="test \n test",
#                 anchor='nw',
#                 textvariable=messchat,
#                 bd=5,
#                 justify=tkinter.LEFT,            
#                 font=("arial", 10),
#                 bg="#ffffff",
#                 fg="#000000",
#                 width=55,
#                 height=10,
#                 relief=tkinter.RIDGE,
#             )
# chat.pack()


# chat.grid(row=0, column=0, sticky=tkinter.W)

# /////////////////////////////////////////////////////////////////////////

scroll = tkinter.Scrollbar(frame2)
scroll.pack(side=tkinter.RIGHT, fill=tkinter.Y)
listbox = tkinter.Listbox(frame2, width=70, yscrollcommand=scroll.set)

listbox.pack(side=tkinter.LEFT)
scroll.config(command=listbox.yview)





#boutons
btn1 = tkinter.Button(frame3, text="Se connecter",font=("arial", 10))
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

btn2 = tkinter.Button(frame3, text="Envoyer",font=("arial", 10), command=envoyer)
# btn2.pack()
btn2.grid(row=1, column=1, sticky=tkinter.W)

frame1.pack(expand=tkinter.YES)
frame2.pack()
frame3.pack(expand=tkinter.YES)


# frame1.grid(row=0, column=0, sticky=tkinter.W)
# frame2.grid(row=60, column=0, sticky=tkinter.W)
# frame3.grid(row=150, column=0, sticky=tkinter.W)

main_frame.pack()

#affichage de la fenetre
fenetre.mainloop()



