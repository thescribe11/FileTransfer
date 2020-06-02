import socket
import os
from tqdm import tqdm
from math import ceil
import sys
import argparse

SERVER_HOST = "0.0.0.0"
SERVER_PORT = 8000
BUFFER_SIZE = 1024 * 5 # 5kb.
SEPERATOR = "<SEP>"

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
WHERE = s.getsockname()[0]
s.close()

def server(path):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((WHERE, SERVER_PORT))
    print("[.] Listening for connections.")
    server.listen(5)
    (client, client_address) = server.accept()
    print("[+] Recieved connection.")
    filesize = os.path.getsize(path)
    try:
        last_loc = path.rindex('\\')
    except ValueError:
        last_loc = -1
    client.send(f"{path[last_loc+1:]}^{filesize}".encode())
    print("[.] Sending file...")
    with open(path, 'rb') as f:
        for i in tqdm(range(ceil(filesize/2048))):
            x = f.read(2048)
            if x == '':
                print("Finished.")
                break
            client.send(x)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="The name of the file you would like to transfer.", nargs="?", default=False)
    
    args = parser.parse_args()

    
    print("""
File Transfer  Copyright (C) 2020  Adam Raschio
This program comes with ABSOLUTELY NO WARRANTY; for details look 
in the LICENSE.TXT file included with your installation.
This is free software, and you are welcome to redistribute it
under certain conditions.

""" )

    filepath = args.filename if args.filename != False else input("Please input the path of the file you would like to transfer.\n")
    if not os.path.isfile(filepath):
        print("*Error*: File does not exist.")
        sys.exit(1)
        
    print(f"File URL: {WHERE}")
    server(filepath)


if __name__ == "__main__":
    main()