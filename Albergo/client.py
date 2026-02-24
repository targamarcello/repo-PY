import socket
import tkinter as tk
from tkinter import messagebox

host = '127.0.0.1'
porta = 50000

# Connessione al server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, porta))

# Richiesta lista camere al server
client.send("LISTA".encode())
risposta = client.recv(2048).decode() #se è andato tutto bene c'è la lista

camere = risposta.split(";")
listaTipi = []

for camera in camere:
    if camera != "":
        tipo, prezzo, disp = camera.split(",")
        listaTipi.append(tipo)#aggiungo la camera 1 alla volta


def prenota():
    testo = entry_notti.get().strip()
    notti = int(testo)

    if notti <= 0:
        messagebox.showerror("Errore", "Le notti devono essere > 0")
        return
    #messaggio di prenotazione al server
    richiesta = "PRENOTA;" + var_camera.get() + ";" + str(notti)
    client.send(richiesta.encode())

    risposta = client.recv(1024).decode()
    parti = risposta.split(";")

    # verifica se il server ha mandato errori
    if parti[0] == "ERRORE":
        messagebox.showerror("Errore", parti[1])
    #verifica se il server ha funzionato correttamente
    elif parti[0] == "OK":
        label_risultato.config(text="Totale: " + parti[1] + " €")


# impostazione interfaccia

interfaccia = tk.Tk()
interfaccia.title("Prenotazione Hotel")
interfaccia.geometry("350x250")

font_base = ("Arial", 12)
#label che serve per la selezione del tipo di camera
tk.Label(interfaccia, text="Seleziona camera:", font=font_base).pack(pady=5)

var_camera = tk.StringVar() #variabile del menù
var_camera.set(listaTipi[0])

menu = tk.OptionMenu(interfaccia, var_camera, *listaTipi)
menu.config(font=font_base)
menu.pack(pady=5)

tk.Label(interfaccia, text="Numero notti:", font=font_base).pack(pady=5)

entry_notti = tk.Entry(interfaccia, font=font_base, justify="center")
entry_notti.pack(pady=5)

#bottone per inviare il comando della prenotazione
tk.Button(interfaccia, text="Prenota", font=font_base, command=prenota).pack(pady=10)

label_risultato = tk.Label(interfaccia, text="", font=("Arial", 13, "bold"))
label_risultato.pack(pady=5)

interfaccia.mainloop()
client.close()