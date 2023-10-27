"""
    - a structural pattern that allows adding new behaviors to object dynamically
    by placing them inside special wrapper objects, called decorators.
"""

from abc import ABC, abstractmethod


class Page(ABC):

    @abstractmethod
    def show(self):
        pass


class AuthPage(Page):

    def show(self):
        print('Welcome to authenticated page...')


class AnonPage(Page):

    def show(self):
        print('Welcome to anonymous page...')


class PageDecorator(Page, ABC):
    def __init__(self, component):
        self._component = component

    @abstractmethod
    def show(self):
        pass


class PageAuthDecorator(PageDecorator):
    def show(self):
        username = input('Enter your username...: ')
        password = input('Enter your password...: ')
        if username == 'admin' and password == 'admin':
            self._component.show()
        else:
            print('you are not authenticated!')


def client():
    page = AuthPage()
    authenticated = PageAuthDecorator(page)
    authenticated.show()


AnonPage().show()

client()
