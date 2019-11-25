# SquallTalk V2

the goal of this python project is to create a communication between two or more device with an GUI as Tkinter.

# How does it work?

1- if you want to make a communication in the same desktop (localhost)

* the "hote" of all client file must have a "localhost" value
* the port number of all files (client et server) must be the same (in this case: 15555)
* I have configure the server file to have a maximum of 4 communicators or clients (4 emission thread and 4 reception thread)
* 1 emission thread and 1 reception thread for each client file
* if you want more communicator duplicate the "client_X.py" file and add as many emission and reception thread that you want communicator


* In the command line, RUN FIRSTLY THE SERVEUR.PY FILE and ONLY AFTER IT the client files, it won't work unless that, the server must be up to exhange messages
* you can run them with the command: "py serveur.py" => "py TheFile"



# Made with purple 💜 lust :-)
