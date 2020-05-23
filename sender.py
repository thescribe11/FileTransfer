import socket
import os
from tqdm import tqdm
from math import ceil

SERVER_HOST = "0.0.0.0"
SERVER_PORT = 8000
BUFFER_SIZE = 1024 * 5 # 5kb.
SEPERATOR = "<SEP>"

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ADDRESS = "localhost:" + (WHERE := s.getsockname()[0]) + ":8000"
s.close()

def server(path):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((WHERE, SERVER_PORT))
    server.listen(5)
    (client, client_address) = server.accept()
    filesize = os.path.getsize(path)
    print(filesize)
    client.send(f"{path}^{filesize}".encode())
    with open(path, 'r') as f:
        for i in tqdm(range(ceil(filesize/1024))):
            x = f.read(1024)
            if x == '':
                print("Finished.")
                break
            client.send(x.encode())

def main():
    filepath = input("Please input the name of the file you would like to transfer.\n> ")
    if not os.path.isfile(filepath):
        print("*Error*: File does not exist.")
        quit(1)
    print(f"File URL: {ADDRESS}")
    server(filepath)


if __name__ == "__main__":
    main()