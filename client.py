import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    message = "Ciao dal client!"
    client_socket.sendall(message.encode())

    data = client_socket.recv(1024).decode()
    print(f"Risposta dal server: {data}")

    client_socket.close()

if __name__ == "__main__":
    start_client()