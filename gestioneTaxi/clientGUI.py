import socket
import tkinter as tk
from tkinter import messagebox

#impostazione di host e porta
host = '127.0.0.1'
porta = 50000

def start_client():
    #definizione della partenza e destinazione
    try:
        dati = text.get("1.0", tk.END).strip()# 1.0 indica la prima riga e il primo carattere
        #creazione del socket del client
        client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        client_socket.connect((host,porta))
        client_socket.sendall(dati.encode())
        #ricezione della risposta dal server
        risposta = client_socket.recv(1024).decode()

        risultato.delete("1.0", tk.END) #pulizia dell'area di testo
        risultato.insert(tk.END, "Dati inviati: " + dati + "\n")
        risultato.insert(tk.END, "Risposta dal server: " + risposta + "\n")
        risultato.see(tk.END)
    
    except socket.error as err:
        messagebox.showerror("Errore", f"Errore di connessione: {err}")

# finestra principale
root = tk.Tk()
root.title("Gestione Taxi")

# zona degli input
label = tk.Label(root, text="Inserisci i dati (partenza,arrivo): ")
label.pack()

text = tk.Text(root, height=10, width=50)
text.pack()
# pulsante di invio
btn = tk.Button(root, text="Invia Dati", command=start_client)
btn.pack()

# area risposta
risultato = tk.Text(root, height=10, width=50)
risultato.pack()
root.mainloop()