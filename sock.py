"""Provides Berkeley socket API originally written in C"""
import socket


host="127.0.0.1"
port=1026
server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM) # set  tcp socket
#print(socket.gethostbyaddr(host))
server_socket.bind((host,port))#server_socket.bind() #associating a socket with a specific network address (IP address and port number) so that it can receive incoming connections or send data to a specific destination

server_socket.listen() # backlog is optional and need to understand 
# synchronous server (take one request send response and then send anoher request)

def synchronous_handling():
    print(f"Server listening on {host}:{port}")
    clientsocket, address = server_socket.accept() # reciving incoming connection and blocking untill
    while True:
        print(f"Connected to {address}")
        data=clientsocket.recv(1024)
        print(data)
        if data==b'\n':
            print("No data send") 
            break
        #print(f"Nahi nahi ! {data.docode()}")

        clientsocket.sendall(f"Nahi nahi app ! {data.decode()}".encode())
               

    print(f"client close having adress:- {address}")   
    clientsocket.close()    

synchronous_handling()



