# Python Server & Cliet 
A simple server written in python with related client
The server and the client run on the same computer

The client accepts textual input and sends it to the server  
The server decodes the message and sends the message back to the client in capitals  
## How to use the server
### Run 
To start the server write the following command in the terminal (Linux)
```
nohup python3 -u server.py & echo $! > run.pid
```
### Read the outputs
To read the output of the server use the following command in the therminal
```
cat nohup.out
```
### Stop the server
To stop the server use the following command in the therminal
```
cat run.pid | xargs kill -9
```

## How to use the client

### Run the client
To run the client open a new termianl an use the following command
```
pythn3 client.py
```
or use your code editor
