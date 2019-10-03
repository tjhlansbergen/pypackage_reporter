import time
import socket

def accept_report():
    # # creeer socket object
    serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

    # hostname en port instellen
    host = socket.gethostname()                           
    port = 9999                                           
    serversock.bind((host, port))                                  

    # luister naar max. 5 requests
    serversock.listen(5)                                           

    while True:
        # establish a connection
        clientsocket,addr = serversock.accept()      

        print("Got a connection from %s" % str(addr))
        currentTime = time.ctime(time.time()) + "\r\n"
        clientsocket.send(currentTime.encode('ascii'))
        clientsocket.close()