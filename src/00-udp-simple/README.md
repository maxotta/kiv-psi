# Simple UDP client and server example

Build the example with the *make* program:

```
$ make
gcc    -c -o client.o client.c
gcc  client.o -o client
gcc    -c -o server.o server.c
gcc  server.o -o server
$ 
```

Start the server:
```
$ ./server 
Server bound to port 8181. Waiting for client's message. Press [Ctrl-C] to interrupt.
```

And run the client in another terminal window:
```
$ ./client 127.0.0.1
Hello message sent, waiting for answer. Press [Ctrl-C] to interrupt.
Server [127.0.0.1] replied: 'Hello from server'
$ 
```
The server will print:
```
Client [127.0.0.1] sent: 'Hello from client !'
Hello message sent.
```
and terminate.

At the end you can clear your workspace with *make clean*
