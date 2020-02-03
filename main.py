import http.server
import socketserver

import argparse
import socket
import time
import sys
import random

import codes

def response_random_code():
    """
        Create and construct string with 200 ok response, headers and response body
        :return string contains response
    """

    L1, L2, L3, L4, L5, L6, L7, L8, L9, L10 = codes.get_all_codes()
    L_All = L1 + L2 + L3 + L4 + L5 + L6 + L7 + L8 + L9 + L10

    random_response_code = random.choice(L_All)
    response = 'HTTP/1.1 ' + random_response_code + '\r\n' + 'Connection: close' + "\r\n\r\n"
    print(response)
    return response


def start(host, port):
    """
        Create socket AF_INET,SOCK_STREAM
        bind to address and port and start listening
    """

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((host, port))
    sock.listen()

    while True:
        current_connection, address = sock.accept()
        # here we wait only one request, size(request) < 2048.
        # after we will blocked on next accept()
        data = current_connection.recv(2048)
        print_data = data.decode()

        resp = response_random_code()
        current_connection.send(resp.encode())
        current_connection.close()

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Listen on host:port, \
                                                  wait for request(< 2048 bytes)',
                                     epilog = 'Example %(prog)s --host 127.0.0.1 --port 8800')

    parser.add_argument("--host", default = "127.0.0.1", type = str,\
                        help = "Host for sending request. Default \"127.0.0.1\"")
    parser.add_argument("--port", default = "8555",      type = int,\
                        help = "Port for sending request. Default \"8555\"")

    args = parser.parse_args()
    host = str(args.host)
    port = int(args.port)

    print('Start listening on ', host, ':', port)

    start(host, port)
