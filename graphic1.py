import tkinter

#couleur d'arrière plan
bgcolor="#d827f0"


#instance de la fenetre principale
window = tkinter.Tk()


#personalisation design fenetre
window.title("SquallTalk V1")
window.maxsize(500,500)
window.minsize(500,500)
window.iconbitmap("squall.ico")
window.config(background=bgcolor)


#delacration frames
frame1 = tkinter.Frame(window, bg=bgcolor)


#widgets?
label_test = tkinter.Label(
                frame1, 
                text="SquallTalk V1", 
                font=("arial", 30),
                bg=bgcolor,
                fg="#ffffff"
            )
label_test.pack()

#bouton
btn1 = tkinter.Button(frame1, text="Se connecter",font=("arial", 10))
btn1.pack()

#empaquetage frames
frame1.pack(expand=tkinter.YES)


#affichage
window.mainloop()