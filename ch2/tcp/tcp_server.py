import socket as skt
import sys


def run_tcp_server():
    server_port = int(sys.argv[1])
    server_socket = skt.socket(skt.AF_INET, skt.SOCK_STREAM)
    server_socket.bind(('', server_port))
    server_socket.listen(1)  # Maximum number of connections

    print('The server is ready to receive')
    while True:
        connection_socket, address = server_socket.accept()
        print('Accept a connection from the client {}'.format(address))
        message = connection_socket.recv(1024)
        capitalized_message = message.upper()
        connection_socket.send(capitalized_message)

        connection_socket.close()


if __name__ == '__main__':
    run_tcp_server()
