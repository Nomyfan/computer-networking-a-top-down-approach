import socket as skt
import sys


def run_udp_server():
    args = sys.argv[1:]
    server_port = int(args[0])

    server_socket = skt.socket(skt.AF_INET, skt.SOCK_DGRAM)
    server_socket.bind(('', server_port))
    print('The server is ready to receive')
    while True:
        message, client_address = server_socket.recvfrom(2048)
        modified_message = message.upper()
        print('Message from client {}'.format(client_address))
        server_socket.sendto(modified_message, client_address)


if __name__ == '__main__':
    run_udp_server()
