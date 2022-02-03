import socket as skt
import sys


def get_server_address():
    args = sys.argv[1:]
    server_hostname = args[0]
    server_port = int(args[1])

    return server_hostname, server_port


def run_udp_client():
    # Use IPv4 and UDP
    client_socket = skt.socket(skt.AF_INET, skt.SOCK_DGRAM)
    message = input('Input lowercase sentence:')
    # Data to send and the destination
    client_socket.sendto(message.encode(), get_server_address())

    modified_message, server_address = client_socket.recvfrom(2048)  # 2048 is the size of the buffer
    print('Message from server {}'.format(server_address))
    print(modified_message.decode())
    client_socket.close()


if __name__ == '__main__':
    run_udp_client()
