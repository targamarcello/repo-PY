import socket
import tkinter as tk
from tkinter import messagebox

host = "127.0.0.1"
porta = 50000


def invia_dati():
    dati = text.get("1.0", tk.END).strip() #strip serve per togliere gli spazi bianchi
    if not dati:
        messagebox.showerror("Errore", "Nessun dato inserito.")
        return
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, porta))
        client_socket.sendall(dati.encode())
        risposta = client_socket.recv(1024).decode()
        client_socket.close()

        risultato.delete("1.0", tk.END)
        risultato.insert(tk.END, risposta)
    except Exception as err:
        messagebox.showerror("Errore: ", err)


# finestra principale
root = tk.Tk()
root.title("Monitoraggio Ambientale")

# zona degli input
label = tk.Label(root, text="Inserisci i dati (data,temp12,temp24): ")
label.pack()

text = tk.Text(root, height=10, width=50)
text.pack()
# pulsante di invio
btn = tk.Button(root, text="Invia Dati", command=invia_dati)
btn.pack()

# area risposta
risultato = tk.Text(root, height=10, width=50)
risultato.pack()
root.mainloop()
