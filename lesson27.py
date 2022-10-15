# Lesson 27 Networking II

import socket
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.connect(('data.pr4e.org',80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
# Chuck lied to me! 
# this following line returns 400 Bad Request
# GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n
mysocket.send(cmd)

while True :
    data = mysocket.recv(512)
    if len(data) < 1 : break
    print(data.decode(),end='')

mysocket.close()

# NOTICE the end='' parameter in the print statement
# Without it text looks funny 

# Experiment 1 >>>>>>> returns bad request
mysocket2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket2.connect(('freecodecamp.org',80))
cmd2 = 'GET https://www.freecodecamp.org/learn/ HTTP/1.0\r\n\r\n'.encode()
mysocket2.send(cmd2)

while True :
    data2 = mysocket2.recv(512)
    if len(data2) < 1 : break
    print(data2.decode(),end='')

mysocket2.close() 