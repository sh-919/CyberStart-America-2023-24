import socket 

text_file = open("backdoor.txt", "r")
text = text_file.read()
text_file.close()
paragraphs = text.split("\n\n")
for x in range(len(paragraphs)):
  paragraphs[x] = paragraphs[x].split("\n")
  for a in range(len(paragraphs[x])):
    paragraphs[x][a] = paragraphs[x][a].split(" ")


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
HOST = 'localhost'
PORT = 10000
s.connect((HOST,PORT))
s.send("any data".encode())

word_codes = s.recv(1024).decode().replace(",","").split("\n")[0:6]
for x in range(len(word_codes)):
  word_codes[x] = word_codes[x].split(" ")

message =""
for a in word_codes: 
  message+=paragraphs[int(a[0])-1][int(a[1])-1][int(a[2])-1].replace(".","").replace("!","").replace(",","").replace("\"","") + "\n"


s.send(message.encode())
print(message)
flag = s.recv(1024).decode()
print(flag)
