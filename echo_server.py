import socket
from threading import Thread
#host=socket.gethostname() #local host
host="localhost"
port=8001
#host="127.0.0.1"
#port=8080
def create_server():
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as server: #create socket for server
        server.bind((host,port)) #bind to IP and port of a server
        server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)# instruct the OS to let us reuse the same bind port
        server.listen()#listen for incoming connection
        clien_connection,addr=server.accept() #addr=[IP,port]
        process(clien_connection,addr)
def process(con,addr):
    with con:
        print(f"{addr} connected")
        while True:
            data=con.recv(4096) #receive data
            if not data: #if data is empty string => ''
                break
            print(data)
            con.sendall(data)#send it back to the client 
def multi_cl_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
         server.bind((host,port))
         server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
         server.listen(2)
         while True :
             clien_connection,addr=server.accept()
             thread= Thread(target=process,args=(clien_connection,addr))
             thread.run()
             
create_server()
#multi_cl_server()