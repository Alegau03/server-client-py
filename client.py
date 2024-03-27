from socket import *
import time
serverName = 'localhost'
serverPort = 65535
clientSocket = socket(AF_INET, SOCK_DGRAM)
#clientSocket.bind(('', 2342)) #random port so we don't use it, bind will be done autom when we send
print("socket created:",clientSocket)
mes=input("Press enter to continue, type 'exit' to exit, type q to stop te server: ")
while mes != "exit":
    if mes == "q":
        message = "q"
        clientSocket.sendto(message.encode(),(serverName, serverPort))
        print("Server is shutting down")
        break  
    else:
        time.sleep(1)
        message = input('Input lowercase sentence: ')
        clientSocket.sendto(message.encode(),(serverName, serverPort))
        print("listening on IP,port:",clientSocket.getsockname())
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        print(modifiedMessage.decode())
        time.sleep(1)
        mes=input("Press enter to continue, type 'exit' to exit, type q to stop te server: ")

clientSocket.close()