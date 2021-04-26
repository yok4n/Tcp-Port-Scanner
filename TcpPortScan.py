import socket
from datetime import datetime

remoteServer = input("adres giriniz: ")
timeout = 0.1
remoteServer_IP_Address = socket.gethostbyname(remoteServer)
print("hedef ıp: " + remoteServer_IP_Address,"Timeout değeri: "+ str(timeout) + "saniye")
zaman_1 = datetime.now()
print("tarama başlama zamanı: " + str(zaman_1))

try:
    for port in range(21,81):
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((remoteServer_IP_Address,port))
        if result == 0:
            print("port: " + str(port) + "açık")
        else:
            print("port: " + str(port)+ "kapalı")
except Exception as error :
    print(str(error))

zaman_2 = datetime.now()
toplam_sure = zaman_2 - zaman_1
print("geçen sure:" +str(toplam_sure))