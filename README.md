This project is a ocal network chat application with a graphical user interface (GUI) built in Python using Tkinter. It includes two main programs:
Chat Server (server_gui.py):
The server allows multiple clients to connect over a local Wi-Fi or LAN network. It displays all chat messages in a scrollable window and lets the server operator send messages to all connected clients. The server uses threading to handle multiple clients at once and broadcasts messages to everyone in the chat.
Chat Client (client_gui.py):
The client provides an easy-to-use interface for connecting to the server. Users enter the server’s IP address, send messages, and see messages from others in real time. The client also uses threading to keep the interface responsive while receiving messages.
Features:
Real-time group chat over a local network.
Simple, user-friendly GUI for both server and client.
No external dependencies—only Python’s standard library is required.
Great for small teams, classrooms, or LAN events.
This project is ideal for learning about socket programming, threading, and GUI development in Python.
