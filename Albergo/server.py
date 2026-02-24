import socket

host = "127.0.0.1"
porta = 50000

camere = {
    "Singola": {"prezzo": 50, "disponibili": 5},
    "Doppia": {"prezzo": 90, "disponibili": 3},
    "Suite": {"prezzo": 150, "disponibili": 2},
}


def calcoloCosto(tipo, notti):
    prezzo = camere[tipo]["prezzo"]
    totale = prezzo * notti

    # Sconto 10%
    if notti >= 7:
        totale = totale * 0.9

    return totale


# Creazione socket server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, porta))
server.listen(5)

print("Server avviato...")

while True:
    conn, addr = server.accept()
    data = conn.recv(1024).decode()
    
    if not data: #il server non riceve nulla
        break

    parti = data.split(";")

    # Richiesta lista camere dal client
    if parti[0] == "LISTA":
        risposta = ""

        for tipo in camere:
            prezzo = camere[tipo]["prezzo"]
            disp = camere[tipo]["disponibili"]
            risposta += tipo + "," + str(prezzo) + "," + str(disp) + ";"

        conn.send(risposta.encode())

    # Richiesta prenotazione dal client
    elif parti[0] == "PRENOTA":

        if len(parti) != 3: #controllo che il formato sia corretto
            conn.send("ERRORE;Formato richiesta non valido".encode())
            continue

        tipo = parti[1]

        # Controllo numero notti
        try:
            notti = int(parti[2])
        except:
            conn.send("ERRORE; Numero notti non valido".encode())
            continue
        if notti <= 0:
            conn.send("ERRORE; Notti devono essere > 0".encode())

        elif tipo not in camere:
            conn.send("ERRORE; Camera inesistente".encode())

        elif camere[tipo]["disponibili"] <= 0:
            conn.send("ERRORE; Camera non disponibile".encode())

        else:
            totale = calcoloCosto(tipo, notti)
            camere[tipo]["disponibili"] -= 1
            conn.send(("OK;" + str(totale)).encode())

conn.close()