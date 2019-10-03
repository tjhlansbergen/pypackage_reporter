import socket

def send_report(report):

    # creeer socket
    clientsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # hostname en port instellen
    host = socket.gethostname()
    port = 9999

    # zet verbinding op
    clientsock.connect((host, port))

    # Receive no more than 1024 bytes
    tm = clientsock.recv(1024)

    # verbinding sluiten
    clientsock.close()

    print("The time got from the server is %s" % tm.decode('ascii'))
