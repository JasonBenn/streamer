import subprocess
import socket

HOST = ''
PORT = 65000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

output = subprocess.Popen(
    "ffmpeg -f avfoundation -i '0:0' -f matroska pipe:1",
    stdout=subprocess.PIPE,
    shell=True
)

with output.stdout as out:
    while True:
        byte = out.read(50)
        if byte:
            s.sendall(byte)
        else:
            break
