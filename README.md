RedCord – Python Networked Chat App

RedCord is a simple real-time chat application built with Python and CustomTkinter. It allows multiple users on the same network (or internet, with proper setup) to send messages to each other through a server-client connection.

Features

Dark mode chat GUI with CustomTkinter 🎨

Connect using server IP – no coding needed for friends

Send messages in real-time with multiple clients

Press Enter or click Send to chat

Lightweight and easy to run

Requirements

Python 3.10+

CustomTkinter

Works on Windows, Mac, Linux

Install dependencies:

pip install customtkinter

How to Use
Step 1 – Run the Server

Open terminal in the project folder.

Run the server:

python server.py


The server will show: Server running on 0.0.0.0:12345.

Step 2 – Run the Client

Open terminal in the project folder.

Run the client:

python client.py


Enter the server IP in the box (e.g., 192.168.1.20) and click Connect.

Type messages in the chat box and press Send or Enter.

Step 3 – Chat with Friends

Your friends can run client.py, enter your IP, and chat with you in real-time.

Note

Works on the same local network by default.

For internet chat, you need to forward port 12345 on your router.

The app is safe, lightweight, and requires no accounts
