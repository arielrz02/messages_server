from socket import *
import threading
import time


def thread_function(sock1, sock2):
    move = sock2.recv(16)
    while move != b'\x00\x00':
        sock1.send(move)
        print(int.from_bytes(move, "big"))
        move = sock2.recv(16)


ip = ""
port = 8888
sock = socket(AF_INET, SOCK_STREAM)
sock.bind((ip, port))
sock.listen(2)
sock1, addr1 = sock.accept()
sock2, addr2 = sock.accept()
x = threading.Thread(target=thread_function, args=(sock1, sock2,))
x.start()
move = sock1.recv(16)
while move != b'\x00\x00':
    sock2.send(move)
    print(int.from_bytes(move, "big"))
    move = sock1.recv(16)
x.join()
sock.close();
"""


ip = ""
port = 8888
sock = socket(AF_INET, SOCK_STREAM)
sock.bind((ip, port))
sock.listen(1)
sock1, addr1 = sock.accept()
for i in range(0, 800):
    sock1.send(i.to_bytes(2, byteorder="big"))
    time.sleep(1/60)
sock.close()
"""