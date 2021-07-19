# Pickle Client Program

import socket
import pickle

HOST = 'player2.acgtest.info'    # The remote host
PORT = 5007              # The same port as used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    #s.sendall(b'Hello, world')
    playerid = 3
    position = 1
    ge = ['play', playerid, position]
    s.send(pickle.dumps(ge))
    data = s.recv(1024)

arr = pickle.loads(data)
print('Received', str(arr))
