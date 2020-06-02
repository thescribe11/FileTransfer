import socket
import tqdm
import math
import os
import sys
import argparse

SEPERATOR = "^"

parser = argparse.ArgumentParser()

parser.add_argument('address', nargs='?', default="False", help="The IP address of the sender.")
parser.add_argument('dir', nargs='?', default="False", help = "The directory where the file should be placed.")

args = parser.parse_args()

sys.stdout.write("""
File Transfer Tools  Copyright (C) 2020  Adam Raschio
This program comes with ABSOLUTELY NO WARRANTY; for details look 
in the LICENSE.TXT file included with your installation.
This is free software, and you are welcome to redistribute it
under certain conditions.

""")

ADDRESS = args.address if args.address != "False" else input("Please input the sender's IPv4 address.\n>")
WRITE_LOC = args.dir if args.dir != "False" else input("\nPlease input the directory you would like the file to be downloaded to (\"1\" for current dir):\n>")
if WRITE_LOC == "1":
    WRITE_LOC = os.getcwd()
PORT = 8000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ADDRESS, PORT))

info = s.recv(1024).decode()
sep_loc = info.find(SEPERATOR)
FILENAME = WRITE_LOC + "\\" + info[0:sep_loc]
print("Writing to", FILENAME, "\n")
filesize = int(info[sep_loc + 1:])

print("Recieving", filesize, "bytes.")

contents = []
for i in tqdm.tqdm(range(math.ceil(filesize/2048))):
    contents.append(s.recv(2048))

print("\nWriting data to file...")

with open(FILENAME, 'wb') as f:
    f.write(b'') # Just to make sure that information doesn't get repeated...

with open(FILENAME, 'a+b') as f:
    for i in tqdm.tqdm(contents):
        f.write(i)

print("\n[+] Done.\n")