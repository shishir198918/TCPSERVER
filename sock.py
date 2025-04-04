"""Provides Berkeley socket API originally written in C"""
import socket


host="127.0.0.1"
port=1026
server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM) # set  tcp socket
#print(socket.gethostbyaddr(host))
server_socket.bind((host,port))#server_socket.bind() #associating a socket with a specific network address (IP address and port number) so that it can receive incoming connections or send data to a specific destination

server_socket.listen() # backlog is optional and need to understand 
print(f"Server listening on {host}:{port}")
# synchronous server (take one request send response and then send anoher request)

def synchronous_handling():    
    while True:
        clientsocket, address = server_socket.accept() # reciving incoming connection and blocking untill        
        print(f"Connected to {address}")
        while True:
            
            data=clientsocket.recv(1024)
            print(data)
            if data==b'\n':
                print("No data send")
                print(f"client close having adress:- {address}")   
                clientsocket.close() 
                break
            #print(f"Nahi nahi ! {data.docode()}")
            clientsocket.sendall(f"hi recived ! {data.decode()}".encode())
               
            

#synchronous_handling()


def data_recv(client_socket,buffer_size ):
    while True:
        data=client_socket.recv(buffer_size)
        if not data:

            break
        yield data



def parse_http(data):
    #paring the request 
    pass
def line_sep(text):
    pass



