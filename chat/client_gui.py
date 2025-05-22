import socket
import threading
import tkinter as tk
from tkinter import simpledialog, scrolledtext

class ClientGUI:
    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        self.root = tk.Tk()
        self.root.title("Wi-Fi Chat Client")

        self.chat_area = scrolledtext.ScrolledText(self.root, wrap=tk.WORD)
        self.chat_area.pack(padx=10, pady=10)
        self.chat_area.config(state='disabled')

        self.msg_entry = tk.Entry(self.root)
        self.msg_entry.pack(padx=10, pady=(0, 10), fill=tk.X)
        self.msg_entry.bind("<Return>", self.send_message)

        self.connect_to_server()
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        self.root.mainloop()

    def connect_to_server(self):
        ip = simpledialog.askstring("Server IP", "Enter server IP address:", parent=self.root)
        self.client_socket.connect((ip, 12345))
        threading.Thread(target=self.receive_messages, daemon=True).start()

    def send_message(self, event=None):
        msg = self.msg_entry.get()
        if msg:
            self.client_socket.send(msg.encode())
            self.msg_entry.delete(0, tk.END)

    def receive_messages(self):
        while True:
            try:
                msg = self.client_socket.recv(1024).decode()
                self.display_message(msg)
            except:
                break

    def display_message(self, msg):
        self.chat_area.config(state='normal')
        self.chat_area.insert(tk.END, msg + "\n")
        self.chat_area.yview(tk.END)
        self.chat_area.config(state='disabled')

    def close(self):
        self.client_socket.close()
        self.root.destroy()

if __name__ == "__main__":
    ClientGUI()
