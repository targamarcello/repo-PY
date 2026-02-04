import socket
#impostazione di host e porta
host = '127.0.0.1'
porta = 50000
#numero dei taxi disponibili
disponibilita = 10

def start_server():
    #creazione del socket del server
    server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_socket.bind((host,porta))
    server_socket.listen(5)
    print("Server in ascolto sulla porta", porta)

    while True:
        #accettazione della connessione dal client
        client_socket, addr = server_socket.accept()
        print("Connessione da:", addr)
        msg = client_socket.recv(1024).decode()
        print("Richiesta ricevuta:", msg)

        global disponibilita 
        if disponibilita > 0:
            disponibilita -= 1
            risposta = "Taxi disponibile. Numero taxi rimanenti: " + str(disponibilita)            
        else:
            risposta = "Nessun taxi disponibile al momento."
        #invio della risposta al client
        client_socket.sendall(risposta.encode())
        #chiusura della connessione
        client_socket.close()

if __name__=="__main__":
    start_server()
