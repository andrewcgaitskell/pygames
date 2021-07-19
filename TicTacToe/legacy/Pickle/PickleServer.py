# Pickle server program
import socket
import pickle

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 5007              # Arbitrary non-privileged port
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            arr = pickle.loads(data)
            print(str(arr))
            if not data: break
            conn.send(pickle.dumps(arr))
            
    s.close()
 
## playerid = 3
## position = 1
## ge = ['play', playerid, position]
## s.send(pickle.dumps(ge))
