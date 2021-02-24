from get_stats import get_all_stat
import socket
from common import send, recv
import time

def connect_to_server(ip, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((ip, port))
    return server

server = connect_to_server("127.0.0.1",4000)


send(server, get_all_stat())
