import socket
import random

host = "127.0.0.1"
porta = 5000
numero_segreto = random.randint(1,100)
print("Numero segreto: ",numero_segreto)

server_socekt = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socekt.bind((host,porta))
server_socekt.listen(2)
print("Server in attesa di una connessione 💤💤💤")

conn,addr = server_socekt.accept()
print(f"Client connesso da {addr}")
while True:
    dato = conn.recv(1024).decode()
    if not dato:
        break
    num = int(dato)
    print("Tentativo del client: ",num)
    if num<numero_segreto:
        risposta = "Troppo basso"
    elif num>numero_segreto:
        risposta = "Troppo alto"
    else:
        risposta = "Corretto"
        conn.sendall(risposta.encode())
        break
    conn.sendall(risposta.encode())
    conn.close()

server_socekt.close()