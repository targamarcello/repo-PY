import socket
import tkinter as tk
from tkinter import messagebox

host = "127.0.0.1"
porta = 5000

# Connessione al server (una sola volta)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, porta))


def invia_numero():
    numero = num.get()

    if not numero.isdigit():
        messagebox.showerror("Errore ⚠️", "Inserisci un numero valido")
        return

    try:
        # Invio del numero al server
        client_socket.sendall(numero.encode())

        # Ricezione risposta
        risposta = client_socket.recv(1024).decode()

        # Mostra risposta nell'area di testo
        area_testo.insert(tk.END, f"Tentativo: {numero}\n")
        area_testo.insert(tk.END, f"Server: {risposta}\n\n")
        area_testo.see(tk.END)

    except:
        messagebox.showerror("Errore ⚠️", "Connessione col server persa")


# ---------------- GUI ----------------

root = tk.Tk()
root.title("Gioco: Indovina il numero")
root.geometry("400x350")

frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

label = tk.Label(frame, text="Inserisci un numero (1-100):")
label.pack()

num = tk.Entry(frame, width=30)
num.pack(pady=5)

btn = tk.Button(frame, text="Prova", command=invia_numero)
btn.pack(pady=5)

area_testo = tk.Text(frame, height=10, width=40)
area_testo.pack(pady=10)

root.mainloop()
