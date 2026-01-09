import socket

HOST = "127.0.0.1"
PORT = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen()
    print("Server in ascolto...")
    while(1):
        conn, addr = server.accept()
        with conn:
            print(f"Connessione da {addr}")
            data = conn.recv(1024).decode()

            print("Messaggio ricevuto dal client:", data)

            risposta = "Messaggio ricevuto correttamente!"
            conn.sendall(risposta.encode())