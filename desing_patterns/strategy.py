"""
    - a behavioral design pattern that lets you define a family of algorithms,
    put each of them into a separate class, and make their objects interchangeable.
"""
from abc import ABC, abstractmethod


class Read:  # context
    def __init__(self, sentence):
        self.sentence = sentence
        self._direction = None  # strategy instance

    def set_direction(self, direction):
        self._direction = direction

    def read(self):
        return self._direction.direct(self.sentence)


class Direction(ABC):  # Abstract Strategy

    @abstractmethod
    def direct(self, data):
        pass


class Right(Direction):  # Concrete Strategy
    def direct(self, data):
        print(data[::-1])


class Left(Direction):  # Concrete Strategy
    def direct(self, data):
        print(data[::1])


c = Read('Hello World')
c.set_direction(Right())
c.read()

c.set_direction(Left())
c.read()
