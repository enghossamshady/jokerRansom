#!/usr/bin/env python3
import base64
import socket
import threading
from threading import Thread
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
keypub = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAnm1TUs+hy4gLOwfHllDY
IHE4nzy+nX99KR3wJkyzg/OFu26We5RVGk0+PmvRlJ+5YG3qpw45K7WW444xRE/h
synm0J8TsfgiUGRoKyvmqAfngNz22mlyjb6cs8UODGuNu9fnsMCjNrROo+gnVAsl
mYTpnfiJFeen7kbHy0/o4ofx6p0sTUkCcRrcXxbXuR0c7mycSA8sE9+ikLXGlec+
YAbtjd97ZNkqFkHVVGp+NTLhx6jTWY1ig7PMAwrg1F/B8sAkWPzlcJxZqIONc5gy
Ad5WwEA5uwIsjiwcYfg4ks8NxW97wi8y2bDbyD9klQSm1VDporJLBa5VX1hVa4Z2
lQIDAQAB
-----END PUBLIC KEY-----  """
#print(keypub)
cipher = PKCS1_OAEP.new(keypub)
keyy = b'\x98\x1c\xfc\xa6|nv\xeff\xeb\xbd\xb5\xd8\xf5\x03\xaf'
encrypted_key = base64.b16encode(keyy)
print(encrypted_key)
# pubkey ="""-----BEGIN PUBLIC KEY-----
# MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAnm1TUs+hy4gLOwfHllDY
# IHE4nzy+nX99KR3wJkyzg/OFu26We5RVGk0+PmvRlJ+5YG3qpw45K7WW444xRE/h
# synm0J8TsfgiUGRoKyvmqAfngNz22mlyjb6cs8UODGuNu9fnsMCjNrROo+gnVAsl
# mYTpnfiJFeen7kbHy0/o4ofx6p0sTUkCcRrcXxbXuR0c7mycSA8sE9+ikLXGlec+
# YAbtjd97ZNkqFkHVVGp+NTLhx6jTWY1ig7PMAwrg1F/B8sAkWPzlcJxZqIONc5gy
# Ad5WwEA5uwIsjiwcYfg4ks8NxW97wi8y2bDbyD9klQSm1VDporJLBa5VX1hVa4Z2
# lQIDAQAB
# -----END PUBLIC KEY-----"""
# pubkey = pubkey.encode("ascii")
# pubkey1 = RSA.importKey(pubkey)
# c = PKCS1_OAEP.new(pubkey1)
# encrypted_key = c.encrypt( b'\x98\x1c\xfc\xa6|nv\xeff\xeb\xbd\xb5\xd8\xf5\x03\xaf')
# print(encrypted_key)
enckey = b'981CFCA67C6E76EF66EBBDB5D8F503AF'

def recvf(c):
    while True:
        data = c.recv(2048)
        if len(data) !=0:
            print(data.decode('ascii'))
def server():
    server_ip = "127.0.0.1"
    port = 4545
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.setblocking(1)
        s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        s.bind((server_ip,port))
        s.listen(1)
        print("waiting for clients ....")
        conn, addr = s.accept()
        print(f"server is running on {server_ip} port {port}")
        t = threading.Thread(target=recvf, args=(conn,))
        t.start()
        command = b'981CFCA67C6E76EF66EBBDB5D8F503AF'
        conn.send(command)
        print("Connected")
        while True:
            command = input("command >> ")
            conn.send(command.encode("ascii"))
            print("Connected")
    except socket.error as e:
        s.close()

server()




#
# class send(Thread):
#     def run(self) -> None:
#         while True:
#             msg = input("inter your msg : ")
#             msg = msg.encode()
#             conn.send(msg)
#             print("your msg is sent .")
# class recive(Thread):
#     def run(self) -> None:
#         while True:
#             r_msg = conn.recv(1024)
#             r_msg = r_msg.decode()
#             print(f"recived msg {r_msg}")
# server()
# t1 = send()
# t2 = recive()
# t1.start()
# t2.start()














# import socket
# ip = 'ca84f2824d572c.lhrtunnel.link'
# host = "192.168.1.9"
# port = 8080
# so = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# so.bind((host,port))
# so.listen(5)
# print("waiting for the connection ......")
# while True:
#     connection, addr = so.accept()
#     print(f"connection successful from addr{addr[0]}")

# import os
# import socket
#
# from pyngrok import ngrok
#
# host = os.environ.get("HOST")
# port = os.environ.get("PORT")
#
#
# # Create a TCP socket
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# # Bind a local socket to the port
# server_address = ("localhost", port)
# sock.bind(server_address)
# sock.listen(1)
#
# # Open a ngrok tunnel to the socket
# public_url = ngrok.connect(port, "tcp", remote_addr="{}:{}".format(host, port)).public_url
# print("ngrok tunnel \"{}\" -> \"tcp://127.0.0.1:{}\"".format(public_url, port))
#
# while True:
#     connection = None
#     try:
#         # Wait for a connection
#         print("\nWaiting for a connection ...")
#         connection, client_address = sock.accept()
#
#         print("... connection established from {}".format(client_address))
#
#         # Receive the message, send a response
#         while True:
#             data = connection.recv(1024)
#             if data:
#                 print("Received: {}".format(data.decode("utf-8")))
#
#                 message = "pong"
#                 print("Sending: {}".format(message))
#                 connection.sendall(message.encode("utf-8"))
#             else:
#                 break
#     except KeyboardInterrupt:
#         print(" Shutting down server.")
#
#         if connection:
#             connection.close()
#         break
#
# sock.close()
#
#
#
