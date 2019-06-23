import socket


hote = "localhost"
port = 15555


socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((hote, port))
print ("Connecté sur le port {}".format(port))


qit=0
while True:
    print("Entrez votre message")
    data=input()
    if "exit" in data:
        qit=1
    data = data.encode("utf8")
    socket.sendall(data)
    #///////////////////////////////////////
    # from_server=socket.recv(255)
    # from_server= from_server.decode("utf8")
    
    # print("reponse du serveur: ",from_server)
    #//////////////////////////////////////////
    if qit==1:
        print ("Déconnecté!")
        socket.close()
        break





