import socket
from threading import *

def receiver(ip1, port1):
    mp = socket.SOCK_DGRAM
    afn = socket.AF_INET
    s = socket.socket(afn, mp)
    s.bind((ip1, port1))
    while True:
        x = s.recvfrom(1024)
        print('Received Message From '+x[1][0]+' : '+x[0].decode())
        print()
        

def sender(ip, port, msg):
    mp = socket.SOCK_DGRAM
    afn = socket.AF_INET
    s = socket.socket(afn, mp)
    s.sendto(msg.encode(), (ip, port))
            

ip1=''
port1 = int(input("Enter Reciever's port number : "))

rec = Thread(target=receiver, args=(ip1, port1))
rec.start()

ip2= input("Enter  sender1 IP address : ")
port2 = int(input("Enter sender1 port number : "))

ip3= input("Enter  sender2 IP address : ")
port3 = int(input("Enter sender2 port number : "))


while True:
    msg=input("$")
    t2=Thread(target=sender, args=(ip2, port2, msg))
    t3=Thread(target=sender, args=(ip3, port3, msg))
    t2.start()
    t3.start()
    print('Your Message To All : ', msg)
