#import socket module
from socket import *
import sys
# In order to terminate the program


def webServer(port=13331):
    serverSocket = socket(AF_INET, SOCK_STREAM)

    #Prepare a sever socket
    serverSocket.bind(("", port))

    serverSocket.listen(1)

    while True:
        # Establish the connection
        # print('Ready to serve...')

        connectionSocket, addr = serverSocket.accept()

        try:
            message = connectionSocket.recv(1024).decode()

            everything = message.split()
            filename = everything[1][1:]
            f = open(filename)

            outputdata = f.read()
            f.close()

            # #Send one HTTP header line into socket
            connectionSocket.send('HTTP/1.1 200 OK\r\n\r\n'.encode())
            # Send the content of the requested file to the client
            # for i in range(0, len(outputdata)):
            #     snd = outputdata[i].encode()
            #     connectionSocket.send(snd)
            connectionSocket.send(outputdata.encode())

            connectionSocket.send("\r\n".encode())
            connectionSocket.close()
        except IOError as e:
            connectionSocket.send('HTTP/1.1 404 Not Found\r\n\r\n'.encode())
            connectionSocket.close()

    serverSocket.close()
    sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
    webServer(13331)
