import socket
ip= "127.0.0.1"
port= 4443
server= socket.socket()
server.bind((ip,port))
print("Server started")
server.listen(1)
client,clientadd=server.accept()
print("Client connected")
while True:
    cmd=input("Enter Command: ")
    cmd=cmd.encode()
    client.send(cmd)
    output=client.recv(1024)
    output=output.decode()
    print(f"\n{output}")

