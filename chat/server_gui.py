import socket
import threading
import tkinter as tk
from tkinter import scrolledtext

# Server configuration
HOST = '0.0.0.0'
PORT = 12345
clients = []

def broadcast(message, sender_socket=None):
    for client in clients.copy():
        if client is not sender_socket:
            try:
                client.send(message.encode())
            except:
                clients.remove(client)

def handle_client(client_socket, addr):
    while True:
        try:
            msg = client_socket.recv(1024).decode()
            if not msg:
                break
            entry = f"({addr[0]}:{addr[1]}) {msg}"
            chat_log.insert(tk.END, entry + "\n")
            chat_log.see(tk.END)
            broadcast(entry, client_socket)
        except:
            break
    client_socket.close()
    if client_socket in clients:
        clients.remove(client_socket)
    chat_log.insert(tk.END, f"[-] {addr} disconnected.\n")
    chat_log.see(tk.END)

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    chat_log.insert(tk.END, f"[*] Server listening on {HOST}:{PORT}\n")
    chat_log.see(tk.END)
    while True:
        client_socket, addr = server.accept()
        clients.append(client_socket)
        chat_log.insert(tk.END, f"[+] {addr} connected.\n")
        chat_log.see(tk.END)
        threading.Thread(target=handle_client, args=(client_socket, addr), daemon=True).start()

def send_message(event=None):
    msg = msg_entry.get().strip()
    if not msg:
        return
    msg_entry.delete(0, tk.END)
    entry = f"(Server) {msg}"
    chat_log.insert(tk.END, entry + "\n")
    chat_log.see(tk.END)
    broadcast(entry)

# GUI setup
root = tk.Tk()
root.title("Wi-Fi Chat Server")
# no external icon needed; Tkinter will use its default window icon

chat_log = scrolledtext.ScrolledText(root, width=60, height=20)
chat_log.pack(padx=10, pady=10)

frame = tk.Frame(root)
frame.pack(fill=tk.X, padx=10, pady=(0,10))

msg_entry = tk.Entry(frame)
msg_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
msg_entry.bind("<Return>", send_message)

send_btn = tk.Button(frame, text="Send", command=send_message)
send_btn.pack(side=tk.RIGHT, padx=(5,0))

# start server thread
threading.Thread(target=start_server, daemon=True).start()

root.mainloop()
