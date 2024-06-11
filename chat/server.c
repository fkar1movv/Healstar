#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <pthread.h>
#include <arpa/inet.h>

#define MAX_CLIENTS 10
#define BUFFER_SIZE 1024
#define PORT 8080

typedef struct {
    struct sockaddr_in address;
    int socket;
    int uid;
    char name[50];
    char role[20];
    int paired_socket;
} client_t;

client_t *clients[MAX_CLIENTS];
pthread_mutex_t clients_mutex = PTHREAD_MUTEX_INITIALIZER;

void print_client_info(client_t *cli) {
    char client_ip[INET_ADDRSTRLEN];
    inet_ntop(AF_INET, &(cli->address.sin_addr), client_ip, INET_ADDRSTRLEN);
    printf("Client connected - IP: %s, Port: %d, Role: %s\n",
           client_ip, ntohs(cli->address.sin_port), cli->role);
}

void add_client(client_t *cl) {
    pthread_mutex_lock(&clients_mutex);

    for (int i = 0; i < MAX_CLIENTS; i++) {
        if (!clients[i]) {
            clients[i] = cl;
            break;
        }
    }

    pthread_mutex_unlock(&clients_mutex);
}

void remove_client(int uid) {
    pthread_mutex_lock(&clients_mutex);

    for (int i = 0; i < MAX_CLIENTS; i++) {
        if (clients[i]) {
            if (clients[i]->uid == uid) {
                clients[i] = NULL;
                break;
            }
        }
    }

    pthread_mutex_unlock(&clients_mutex);
}

void pair_clients() {
    pthread_mutex_lock(&clients_mutex);

    for (int i = 0; i < MAX_CLIENTS; i++) {
        if (clients[i] && strcmp(clients[i]->role, "doctor") == 0 && clients[i]->paired_socket == 0) {
            for (int j = 0; j < MAX_CLIENTS; j++) {
                if (clients[j] && strcmp(clients[j]->role, "patient") == 0 && clients[j]->paired_socket == 0) {
                    clients[i]->paired_socket = clients[j]->socket;
                    clients[j]->paired_socket = clients[i]->socket;
                    printf("Doctor (ID: %d) and Patient (ID: %d) paired.\n", clients[i]->uid, clients[j]->uid);
                    break;
                }
            }
        }
    }

    pthread_mutex_unlock(&clients_mutex);
}

void *handle_client(void *arg) {
    char buffer[BUFFER_SIZE];
    int leave_flag = 0;
    client_t *cli = (client_t *)arg;

    print_client_info(cli); // Print client information

    // Receive role
    if (recv(cli->socket, cli->role, sizeof(cli->role), 0) <= 0) {
        leave_flag = 1;
    } else {
        printf("Role received: %s\n", cli->role);
        pair_clients();
    }

    // Receiving name
    if (recv(cli->socket, cli->name, sizeof(cli->name), 0) <= 0) {
        leave_flag = 1;
    } else {
        printf("Name received: %s\n", cli->name);
    }

    bzero(buffer, BUFFER_SIZE);

    while (1) {
        if (leave_flag) {
            break;
        }

        int receive = recv(cli->socket, buffer, BUFFER_SIZE, 0);
        if (receive > 0) {
            if (strlen(buffer) > 0) {
                // Send message to paired client
                char send_buffer[BUFFER_SIZE + 70];
                if (cli->paired_socket != 0) {
                    sprintf(send_buffer, "%s (%s): %s", cli->name, cli->role, buffer);
                    send(cli->paired_socket, send_buffer, strlen(send_buffer), 0);
                }
            }
        } else if (receive == 0 || strcmp(buffer, "exit") == 0) {
            printf("Client (ID: %d) disconnected.\n", cli->uid);
            leave_flag = 1;
        } else {
            printf("ERROR: -1\n");
            leave_flag = 1;
        }

        bzero(buffer, BUFFER_SIZE);
    }

    close(cli->socket);
    remove_client(cli->uid);
    free(cli);
    pthread_detach(pthread_self());

    return NULL;
}

int main() {
    int listenfd = 0, connfd = 0;
    struct sockaddr_in serv_addr, cli_addr;
    pthread_t tid;

    // Socket settings
    listenfd = socket(AF_INET, SOCK_STREAM, 0);
    serv_addr.sin_family = AF_INET;
    serv_addr.sin_addr.s_addr = inet_addr("192.168.17.133");
    serv_addr.sin_port = htons(PORT);

    // Bind
    if (bind(listenfd, (struct sockaddr*)&serv_addr, sizeof(serv_addr)) < 0) {
        perror("Socket binding failed");
        return 1;
    }

    // Listen
    if (listen(listenfd, 10) < 0) {
        perror("Socket listening failed");
        return 1;
    }

    printf("<[ SERVER STARTED ]>\n");

    // Accept clients
    while (1) {
        socklen_t clilen = sizeof(cli_addr);
        connfd = accept(listenfd, (struct sockaddr*)&cli_addr, &clilen);

        // Check for max clients
        if ((connfd + 1) == MAX_CLIENTS) {
            printf("Max clients reached. Connection rejected.\n");
            close(connfd);
            continue;
        }

        // Client settings
        client_t *cli = (client_t *)malloc(sizeof(client_t));
        cli->address = cli_addr;
        cli->socket = connfd;
        cli->uid = connfd;
        cli->paired_socket = 0;

        // Add client to the array
        add_client(cli);

        // Create thread
        pthread_create(&tid, NULL, &handle_client, (void*)cli);

        // Reduce CPU usage
        sleep(1);
    }

    return 0;
}