import customtkinter as ctk
import socket
import threading

# ------------------ Networking ------------------
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def connect_to_server(ip, port=12345):
    try:
        client.connect((ip, port))
        messages.insert("end", f"Connected to {ip}\n")
        threading.Thread(target=receive_messages, daemon=True).start()
        connect_btn.configure(state="disabled")
        ip_entry.configure(state="disabled")
    except:
        messages.insert("end", f"Failed to connect to {ip}\n")

def receive_messages():
    while True:
        try:
            msg = client.recv(1024).decode()
            if msg:
                messages.insert("end", msg + "\n")
                messages.see("end")
        except:
            break

def send_message():
    msg = msg_entry.get().strip()
    if msg:
        client.send(msg.encode())
        msg_entry.delete(0, "end")

# ------------------ GUI ------------------
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

BG_MAIN = "#1e0000"
RED = "#ff2b2b"
TEXT = "#ffffff"
BOX = "#2a0000"

app = ctk.CTk()
app.geometry("700x500")
app.title("RedCord Networked Chat")

# Chat messages
messages = ctk.CTkTextbox(app, fg_color=BOX, text_color=TEXT)
messages.pack(fill="both", expand=True, padx=10, pady=10)
messages.insert("end", "Welcome to RedCord 🔥\n")

# IP input frame
ip_frame = ctk.CTkFrame(app, fg_color=BG_MAIN)
ip_frame.pack(fill="x", padx=10, pady=(0,5))

ctk.CTkLabel(ip_frame, text="Enter Server IP:", text_color=TEXT).pack(side="left", padx=(0,5))
ip_entry = ctk.CTkEntry(ip_frame, placeholder_text="e.g., 192.168.1.20", fg_color=BOX)
ip_entry.pack(side="left", fill="x", expand=True, padx=(0,5))
connect_btn = ctk.CTkButton(ip_frame, text="Connect", fg_color=RED, hover_color="#ff5555",
                            command=lambda: connect_to_server(ip_entry.get()))
connect_btn.pack(side="right")

# Message input frame
input_frame = ctk.CTkFrame(app, fg_color=BG_MAIN)
input_frame.pack(fill="x", padx=10, pady=10, side="bottom")

msg_entry = ctk.CTkEntry(input_frame, placeholder_text="Message...", fg_color=BOX)
msg_entry.pack(side="left", fill="x", expand=True, padx=(0, 10))

send_btn = ctk.CTkButton(input_frame, text="Send", fg_color=RED, hover_color="#ff5555", command=send_message)
send_btn.pack(side="right")

# Press Enter to send message
msg_entry.bind("<Return>", lambda event: send_message())

app.mainloop()
