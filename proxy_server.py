import socket
from threading import Thread
phost="127.0.0.1"
pport=8080
def send_request(host, port,request):
    
    # Create a socket object
    with  socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:

        # Connect to the remote server)
        client_socket.connect((host, port))

        # Send an HTTP GET request for the root path ("/")
        client_socket.send(request)
        #finish sending data
        client_socket.shutdown(socket.SHUT_WR)

        # Receive and print the response from the server
        response = b""
        while True:
            data = client_socket.recv(4096)
            if not data:
                break
            response += data

        return response
def process(con,addr):
    with con:
        print(f"{addr} connected")
        request=b""      #data recieve is always byte type
        while True:
            data=con.recv(4096) #receive data
            if not data: #if data is empty string => break
                break
            print(data)
            request+=data #append received data 
        response= send_request('www.google.com',80,request) #send data received from client to google
        con.sendall(response) #send it back to the client 
def start_server():
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as server: #create socket for server
        server.bind((phost,pport)) #bind to IP and port of a server
        server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)# instruct the OS to let us reuse the same bind port
        server.listen()#listen for incoming connection
        clien_connection,addr=server.accept() #addr=[IP,port]
        process(clien_connection,addr)
def multi_cl_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
         server.bind((phost,pport))
         server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
         server.listen(2) #allow up to 2 connection and put in queue
         while True :
             clien_connection,addr=server.accept()
             thread= Thread(target=process,args=(clien_connection,addr))
             thread.run()
#start_server()
multi_cl_server()
