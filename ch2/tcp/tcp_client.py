import socket as skt
import sys


def get_server_address():
    args = sys.argv[1:]
    server_hostname = args[0]
    server_port = int(args[1])

    return server_hostname, server_port


def run_tcp_client():
    client_socket = skt.socket(skt.AF_INET, skt.SOCK_STREAM)
    client_socket.connect(get_server_address())

    message = input('Input lowercase sentence:')
    client_socket.send(message.encode())

    modified_message = client_socket.recv(1024)
    print('Message from server:{}'.format(modified_message.decode()))

    client_socket.close()


if __name__ == '__main__':
    run_tcp_client()
