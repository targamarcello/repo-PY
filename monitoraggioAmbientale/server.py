import socket

# impostazione host e porta
host = "127.0.0.1"
porta = 50000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, porta))
server_socket.listen(5)
print(f"Server in ascolto su {host}:{porta}")

while True:
    client, addr = server_socket.accept()
    dati = client.recv(1024).decode()
    righe = dati.strip().split("\n")
    temperature = []
    for riga in righe:
        try:
            data, t12, t24 = riga.split(";")
            t12 = float(t12)
            t24 = float(t24)
            temperature.append(t12)
            temperature.append(t24)
        except:
            continue
    num_igorni = len(temperature) // 2
    num_rilevazioni = len(temperature)
    media = sum(temperature) / num_rilevazioni
    massima = max(temperature)
    minima = min(temperature)
    risposta = (
        f"Numero giorni analizzati : {num_igorni}\n"
        f"Numero rilevazioni : {num_rilevazioni}\n"
        f"Temperatura media : {media}\n"
        f"Temperatura massima : {massima}\n"
        f"Temperatura minima : {minima}\n"
    )
    client.sendall(risposta.encode())
    # chiusura connessione
    client.close()