# Write a script that connects to 'localhost' port 10000
# You then need to send a command to list the files in the /tmp directory

import socket

host = "localhost"
port = 10000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.connect((host, port))
  s.send(b"ls /tmp")
  data = s.recv(1024)
  s.close()
  
print(data)
