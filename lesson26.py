# Lesson 26 Networking with Python

import socket
print(socket)
print(dir(socket))

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(mysocket.connect(('data.pr4e.org', 80))) # returns None wich is better than traceback :)