import socket
host='localhost'
port=9000
s=socket.socket()
s.connect((host,port))
print("enter the -1 to terminate the connection ")
print("enter the message ")
sdata=input()
while (sdata!="-1"):
    s.send(sdata.encode())
    rdata=s.recv(1024)
    print("message from server ",rdata.decode())
    print("enter the message ")
    sdata=input()
s.close()
    
