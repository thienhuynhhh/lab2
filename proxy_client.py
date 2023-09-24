import socket

def send_request(host, port):
    request = "GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n"
    # Create a socket object
    with  socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:

        # Connect to the remote server)
        client_socket.connect((host, port))

        # Send an HTTP GET request for the root path ("/")
        client_socket.send(request.encode())
        #finish sending data
        client_socket.shutdown(socket.SHUT_WR)

        # Receive and print the response from the server
        response = b""
        while True:
            data = client_socket.recv(4096)
            if not data:
                break
            response += data

        print(response)

    # Close the socket connection
    client_socket.close()
send_request("127.0.0.1",8080)
send_request("127.0.0.1",8080)