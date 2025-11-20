"""A program that responds to network connections by sending a random quote"""

import random
import socket

QUOTES = ["I love Fortnite.", "I love London.", "I want Chic-Fil-a peppermint milkshake.", "I am super hungry."]
SERVER_NAME = "Gabe Server"
PORT = 21670

s = socket.socket() #An instance of a socket class
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("0.0.0.0", PORT)) #Ask the OS to create a socket on this computer
s.listen()
print(f"Server started on port {PORT}")

while True: #We'll kill our app with CTRL+C
    conn, addr = s.accept()
    quote = random.choice(QUOTES)
    print(f"Sending a random message to {addr[0]}: {quote}")
    conn.send(quote.encode())
    conn.close()