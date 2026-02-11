import socket
import tkinter as tk
from tkinter import messagebox

HOST = '127.0.0.1'
PORT = 5000


# ===== CONNESSIONE AL SERVER PER OTTENERE LA LISTA FILM =====
# Il client si connette al server e invia la richiesta "LISTA".
# Il server risponde con una stringa contenente tutti i film disponibili.

try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))
    client.send("LISTA".encode())

    data = client.recv(4096).decode()   # Ricezione lista film
    client.close()

except:
    print("Server non attivo")
    exit()


# ===== ELABORAZIONE DELLA RISPOSTA DEL SERVER =====
# La lista arriva nel formato:
# nome,posti,prezzo;nome,posti,prezzo;...
# Qui estraiamo solo il nome del film per mostrarlo nel menu.

film_data = []
film_list = data.split(";")

for film in film_list:
    if film != "":
        parti = film.split(",")
        nome = parti[0]
        film_data.append(nome)

if len(film_data) == 0:
    print("Nessun film ricevuto")
    exit()


# ===== FUNZIONE DI ACQUISTO =====
# Quando l’utente clicca "Acquista":
# 1) Il client invia al server: ACQUISTA;film;numero
# 2) Il server calcola totale e sconto
# 3) Il client riceve e mostra il risultato

def acquista():
    film = film_var.get()
    biglietti = entry_biglietti.get()

    # Controllo che l'input sia un numero valido
    if not biglietti.isdigit():
        messagebox.showerror("Errore", "Inserisci un numero valido")
        return

    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((HOST, PORT))

        messaggio = "ACQUISTA;" + film + ";" + biglietti
        client.send(messaggio.encode())

        risposta = client.recv(1024).decode()
        client.close()

        parti = risposta.split(";")

        # Se il server invia un errore lo mostriamo
        if parti[0] == "ERRORE":
            messagebox.showerror("Errore", parti[1])
        else:
            totale = float(parti[0])
            sconto = float(parti[1])
            finale = float(parti[2])

            # Visualizzazione del risultato finale
            risultato_label.config(
                text="Totale: € {:.2f}\nSconto: € {:.2f}\nDa pagare: € {:.2f}".format(
                    totale, sconto, finale
                )
            )

    except:
        messagebox.showerror("Errore", "Connessione fallita")


# ===== CREAZIONE INTERFACCIA GRAFICA =====
# L'interfaccia permette:
# - selezione del film
# - inserimento numero biglietti
# - visualizzazione risultato

root = tk.Tk()
root.title("Biglietteria Cinema")
root.geometry("500x350")

tk.Label(root, text="BIGLIETTERIA CINEMA",
         font=("Arial", 18)).pack(pady=15)

film_var = tk.StringVar(root)
film_var.set(film_data[0])

menu = tk.OptionMenu(root, film_var, *film_data)
menu.config(font=("Arial", 12), width=20)
menu.pack(pady=10)

entry_biglietti = tk.Entry(root, font=("Arial", 14))
entry_biglietti.pack(pady=10)

tk.Button(root, text="Acquista",
          font=("Arial", 12),
          width=20,
          command=acquista).pack(pady=10)

risultato_label = tk.Label(root, text="", font=("Arial", 12))
risultato_label.pack(pady=20)

root.mainloop()
