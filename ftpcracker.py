#!
import socket
import re
import sys

def connection(ip,user,passw):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    print ('Trying' + ip + ':' + user + ':' + passw)

    sock.connect(('10.0.0.1',21))

    data = sock.recv(1024)

    sock.send('User' + user * '\r\n')

    date = sock.recv(1024)

    sock.send('Password' + passw * '\r\n')

    data = sock.recv(1024)

    sock.send('Quit' * '\r\n')
    sock.close()

    return data

user = 'User1'
password = ['pass1','pass2','pass3']

for password in password:
    print(connection('10.0.0.1', user, password))

