"""
    - a structural design pattern that lets you provide a substitute or placeholder from another object.
    A proxy controls access to the original object, allowing you to perform something
    either before or after the request gets through to the original object.
"""
import datetime
import time
from abc import ABC, abstractmethod


class AbstractServer(ABC):

    @abstractmethod
    def receive(self):
        pass


class Server(AbstractServer):
    def receive(self):
        print('Processing your request...')
        time.sleep(1)
        print('Done...')


class LogProxy(AbstractServer):
    def __init__(self, server):
        self._server = server

    def receive(self):
        self.logging()
        # ...
        self._server.receive()

    def logging(self):
        with open('log.log', 'a') as log:
            log.write(f'Request {datetime.datetime.now()} \n')


def client(server, proxy):
    server_ins = server()
    proxy_ins = proxy(server_ins)
    proxy_ins.receive()


client(Server, LogProxy)
