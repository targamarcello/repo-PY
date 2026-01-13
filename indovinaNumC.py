import socket
host = "127.0.0.1"
porta = 5000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host,porta))
print("Client connesso al server")
while True:
    numero = input("Inserisci un numero (1-100): ")
    client_socket.sendall(numero.encode())

    risposta = client_socket.recv(1024).decode()
    print("Risposta dal server: ",risposta)

    if risposta == "Corretto":
        print("Hai indovinato!!🧙")
        break

client_socket.close()