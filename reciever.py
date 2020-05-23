import socket
import tqdm
import math

SEPERATOR = "^"

ADDRESS = input("Please input the sender's IPv4 address.\n>")
WRITE_LOC = input("\nPlease input the directory you would like the file to be downloaded to:\n>")
PORT = 8000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ADDRESS, PORT))

info = s.recv(1024).decode()
sep_loc = info.find(SEPERATOR)
FILENAME = info[0:sep_loc]
print(FILENAME)
filesize = int(info[sep_loc + 1:])

print("The size of the file is: ", filesize)

contents = []
for i in tqdm.tqdm(range(math.ceil(filesize))):
    contents.append(s.recv(1024).decode())

fullstr = ''.join(contents).encode()
print(fullstr)

with open(FILENAME, 'w+b') as f:
    f.write(fullstr)

print("[+] Done.")
