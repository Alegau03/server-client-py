from socket import *
serverPort = 65535
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print("The server is ready to receive on port "+str(serverPort))
while True:
  message, clientAddress = serverSocket.recvfrom(2048)
  if message.decode() == "q":
    print("Server is shutting down")
    break
  elif message.decode()=="ping":
    modifiedMessage="pong"
  else:
    modifiedMessage = message.decode().upper()
  print("received:",message,'from',clientAddress)
  print("sending: "+modifiedMessage)
  serverSocket.sendto(modifiedMessage.encode(), clientAddress)