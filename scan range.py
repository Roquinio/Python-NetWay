from threading import Thread 
import socket


def scan_range():    #Définir la fonction du scan des ports
    
    ip = ["127.0.0.1","192.168.0.1"]      # Attribution de la plage d'adresse
    for i in ip :
        for port in range(1, 1025):     # Parcours de la plage des ports
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        # Création d'un socket pour la connexion avec le serveur en local
            result = sock.connect_ex((i,port))      # connexion au serveur, bloc surveillé, et gestion de l'exception
            if 0 == result:
                print("Port: {} Ouvert".format(port))
            sock.close()

scan_range()

try:
    thread.start_new_thread (scan_range, ("Thread-1", 2, ) )
    thread.start_new_thread (scan_range, ("Thread-2", 4, ) )

except:
   print ("Erreur")

while 1:
   pass
