import socket
print("simple chat application ")
host='localhost'
port=9000
s=socket.socket()
s.bind((host,port))
s.listen(1)
c,addr=s.accept()
print("a client is connected ")
while True:
    rdata=c.recv(1024)
    if not rdata:
        break;
    print("message from clien : ",rdata.decode())
    print("enter the message ")
    sdata=input()
    c.send(sdata.encode())
c.close()
