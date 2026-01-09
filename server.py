import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 12345))  # Indirizzo e porta
    server_socket.listen(5)
    print("Server in ascolto sulla porta 12345...")
    while(1):
        conn, addr = server_socket.accept()
        print(f"Connessione stabilita con {addr}")

        data = conn.recv(1024).decode()
        print(f"Messaggio ricevuto: {data}")

        response = "Ciao dal server!"
        conn.send(response.encode())

        conn.close()
    
    server_socket.close()

if __name__ == "__main__":
    start_server()