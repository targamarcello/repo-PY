import socket

HOST = '127.0.0.1'
PORT = 5000

# Database dei film:
# per ogni film salviamo [posti_disponibili, prezzo_biglietto]
film_db = {
    "Avatar 2": [50, 8.0],
    "Oppenheimer": [40, 7.5],
    "Barbie": [30, 6.0]
}

# Funzione che calcola lo sconto in base al numero di biglietti
def calcola_sconto(n, totale):
    if n >= 5:
        return totale * 0.10   # 10% di sconto
    elif n >= 3:
        return totale * 0.05   # 5% di sconto
    return 0                  # nessuno sconto


# Creazione del socket TCP del server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Associa il server a indirizzo e porta
server.bind((HOST, PORT))

# Il server si mette in ascolto di richieste client
server.listen(1)

print("Server avviato...")


# Ciclo infinito: il server resta sempre attivo
while True:
    conn, addr = server.accept()  # Accetta una connessione
    print("Connesso:", addr)

    try:
        # Riceve la richiesta del client
        richiesta = conn.recv(1024).decode()
        parti = richiesta.split(";")

        # ===== PROTOCOLLO DI COMUNICAZIONE =====
        # Il client può inviare:
        # 1) "LISTA"
        # 2) "ACQUISTA;film;numero"

        # --- Caso 1: richiesta lista film ---
        if parti[0] == "LISTA":
            risposta = ""

            # Costruisce la stringa nel formato:
            # nome,posti,prezzo;nome,posti,prezzo;...
            for nome in film_db:
                posti = film_db[nome][0]
                prezzo = film_db[nome][1]
                risposta += nome + "," + str(posti) + "," + str(prezzo) + ";"

            conn.send(risposta.encode())

        # --- Caso 2: richiesta acquisto ---
        elif parti[0] == "ACQUISTA":
            film = parti[1]
            num_biglietti = int(parti[2])

            # Controllo numero valido
            if num_biglietti <= 0:
                conn.send("ERRORE;Numero non valido".encode())

            # Controllo disponibilità posti
            elif film_db[film][0] < num_biglietti:
                conn.send("ERRORE;Biglietti non disponibili".encode())

            else:
                # Calcolo totale e sconto
                prezzo = film_db[film][1]
                totale = prezzo * num_biglietti
                sconto = calcola_sconto(num_biglietti, totale)
                finale = totale - sconto

                # Aggiornamento posti disponibili
                film_db[film][0] -= num_biglietti

                # Risposta nel formato:
                # totale;sconto;finale
                risposta = str(totale) + ";" + str(sconto) + ";" + str(finale)
                conn.send(risposta.encode())

    except:
        # Gestione errore generico di richiesta malformata
        conn.send("ERRORE;Richiesta non valida".encode())

    # Chiusura connessione con il client
    conn.close()
