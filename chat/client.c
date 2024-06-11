#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/socket.h>
#include <arpa/inet.h>

#define PORT 8080
#define BUFFER_SIZE 1024

int main() {
    struct sockaddr_in server_addr;
    int sock;
    char buffer[BUFFER_SIZE];
    char role[20];
    char name[50];

    // Create socket
    sock = socket(AF_INET, SOCK_STREAM, 0);
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(PORT);
    server_addr.sin_addr.s_addr = inet_addr("192.168.17.133");

    // Connect to server
    if (connect(sock, (struct sockaddr *)&server_addr, sizeof(server_addr)) < 0) {
        perror("Connection failed");
        return 1;
    }

    printf("Connected to server.\n");

    // Enter role and name
    printf("Enter your role (doctor/patient): ");
    fgets(role, sizeof(role), stdin);
    role[strcspn(role, "\n")] = 0; // Remove newline character
    send(sock, role, sizeof(role), 0);

    printf("Enter your name: ");
    fgets(name, sizeof(name), stdin);
    name[strcspn(name, "\n")] = 0; // Remove newline character
    send(sock, name, sizeof(name), 0);

    // Communication with server
    while (1) {
        printf("You: ");
        fgets(buffer, BUFFER_SIZE, stdin);
        buffer[strcspn(buffer, "\n")] = 0; // Remove newline character

        if (strcmp(buffer, "exit") == 0) {
            break;
        }

        send(sock, buffer, strlen(buffer), 0);
        memset(buffer, 0, BUFFER_SIZE);
        if (recv(sock, buffer, BUFFER_SIZE, 0) > 0) {
            printf("%s\n", buffer);
        }
    }

    close(sock);
    printf("Disconnected from server.\n");

    return 0;
}
