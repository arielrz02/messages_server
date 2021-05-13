from socket import *
import threading


def thread_function(sock):
    num1 = -1
    while num1 != 0:
        num1 = int(input("input num"))
        _num1 = num1.to_bytes(2, "big")
        sock.send(_num1)


ip = "127.0.0.1"
port = 8888
sock = socket(AF_INET, SOCK_STREAM)
sock.connect((ip, port))
x = threading.Thread(target=thread_function, args=(sock,))
x.start()
first = -1
while first != b'':
    first = sock.recv(128)
    print(int.from_bytes(first, byteorder="big"))
x.join()
sock.close()

