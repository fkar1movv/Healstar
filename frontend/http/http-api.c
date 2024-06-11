#include "http/http-api.h"
#include <stdbool.h>

#define BUF_SIZE 1024

int http_init(struct http *dst, char *host, in_port_t port)
{
    strncpy(dst->hostname, host, sizeof(dst->hostname));
    dst->port = port;
    return 0; // Return a status, typically 0 for success
}

static int _http_response(int fd, char **dst_body, unsigned int *buf_size)
{
    FILE *fp = fdopen(fd, "r");
    if (!fp) return -1; // Handle fdopen failure

    char *lineptr = NULL;
    size_t line_length = 0;
    int ret_code = -1; // Default to error
    bool header_end = false;

    // Fetching header
    while(getline(&lineptr, &line_length, fp) != -1)
    {
        if (strstr(lineptr, "HTTP/"))
        {
            char *code_start = strchr(lineptr, ' ');
            if (code_start) ret_code = atoi(code_start + 1);
        }
        else if(strcmp(lineptr, "\r\n") == 0)
        {
            header_end = true;
            break;
        }
    }
    free(lineptr);
    if (!header_end) return -1; // Handle missing header end

    // Reading response body
    *buf_size = BUF_SIZE;
    *dst_body = malloc(*buf_size);
    if (!*dst_body) return -1; // Handle malloc failure

    size_t total_bytes = 0;
    size_t n_read;
    while((n_read = fread(*dst_body + total_bytes, 1, BUF_SIZE, fp)) > 0)
    {
        total_bytes += n_read;
        if(total_bytes >= *buf_size)
        {
            *buf_size *= 2;
            *dst_body = realloc(*dst_body, *buf_size);
            if (!*dst_body) return -1; // Handle realloc failure
        }
    }

    fclose(fp);
    close(fd);
    return ret_code;
}

// Combined HTTP request function
int http_request(struct http *dst, const char *method, const char *route, 
                 const char *body, unsigned int body_size, 
                 char **response_body, unsigned int *response_body_size)
{
    int fd = user_socket_connect(dst->hostname, dst->port);
    if (fd == -1)
    {
        fprintf(stderr, "Socket failure\n");
        return -1;
    }

    char buffer[BUF_SIZE];
    int pos = snprintf(buffer, BUF_SIZE, "%s %s HTTP/1.0\r\n", method, route);
    if (body && body_size > 0)
    {
        pos += snprintf(buffer + pos, BUF_SIZE - pos, "Content-Type: application/json\r\n");
        pos += snprintf(buffer + pos, BUF_SIZE - pos, "Content-Length: %u\r\n", body_size);
    }
    pos += snprintf(buffer + pos, BUF_SIZE - pos, "\r\n");

    if (write(fd, buffer, pos) != pos || (body && write(fd, body, body_size) != body_size))
    {
        fprintf(stderr, "Write func failure\n");
        close(fd);
        return -1;
    }

    return _http_response(fd, response_body, response_body_size);
}

int http_get(struct http *dst, char *route, char **response_body, unsigned int *response_body_size)
{
    return http_request(dst, "GET", route, NULL, 0, response_body, response_body_size);
}

int http_post(struct http *dst, char *route, char *post_body, unsigned int post_body_size, 
              char **response_body, unsigned int *response_body_size)
{
    return http_request(dst, "POST", route, post_body, post_body_size, response_body, response_body_size);
}
