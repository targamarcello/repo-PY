import socket
#impostazione di host e porta
host = '127.0.0.1'
porta = 50000

def start_client():
    #definizione della partenza e destinazione
    partenza = input("Inserisci la città di partenza: ")
    destinazione = input("Inserisci la città di destinazione: ")

    msg = partenza+ " - " + destinazione

    try:
        #creazione del socket del client
        client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        client_socket.connect((host,porta))
        client_socket.sendall(msg.encode())
        #ricezione della risposta dal server
        risposta = client_socket.recv(1024).decode()
        print("Risposta del server: ",risposta)
        #chiusura socket
        client_socket.close()
    except socket.error as err:
        print("Errore: ",err)

if __name__=="__main__":
    start_client()