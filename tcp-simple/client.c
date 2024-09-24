// Client side C program to demonstrate Socket
// programming
#include <arpa/inet.h>
#include <stdio.h>
#include <stdlib.h> 
#include <string.h>
#include <sys/socket.h>
#include <unistd.h>
#define PORT 8080

int main(int argc, char const* argv[])
{
    int status, valread, client_fd;
	struct sockaddr_in server;
	in_addr_t server_address;
    char* hello = "Hello from client";
    char buffer[1024] = { 0 };

	if (argc != 2) {
		printf("Usage: %s <IP v4 address>\n", argv[0]);
		exit(1);
	}

	// Convert dotted quad notation to a sockaddr_in address structure
	if ((server_address = inet_addr(argv[1])) < 0) {
		printf("Invalid address '%s' !\n", argv[1]);
		exit(EXIT_FAILURE);
	}

    if ((client_fd = socket(AF_INET, SOCK_STREAM, 0)) < 0) {
        printf("\n Socket creation error \n");
        return -1;
    }

	// Fill in the server information
	server.sin_family      = AF_INET;            // Address Family Internet IPv4
	server.sin_port        = htons(PORT);        // Server's Port
	server.sin_addr.s_addr = server_address;     // Server's Address

    if ((status
         = connect(client_fd, (struct sockaddr*)&server,
                   sizeof(server)))
        < 0) {
        printf("\nConnection Failed \n");
        return -1;
    }
    send(client_fd, hello, strlen(hello), 0);
    printf("Hello message sent\n");
    valread = read(client_fd, buffer,
                   1024 - 1); // subtract 1 for the null
                              // terminator at the end
    printf("%s\n", buffer);

    // closing the connected socket
    close(client_fd);
    return 0;
}
