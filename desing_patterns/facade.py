"""
    - a structural design pattern that provides a simplified interface to a library,
    a framework, or any other complex set of classes.
"""


class CPU:
    def execute(self):
        print('Executing...')


class Memory:
    def load(self):
        print('Loading data...')


class SSD:
    def read(self):
        print('Some data from ssd')


class Computer:  # Facade
    def __init__(self, sub1, sub2):
        self.cpu = sub1()
        self.memory = sub2()

    def start(self):
        self.cpu.execute()
        self.memory.load()

    # def __init__(self): # other form
    #     self.cpu = CPU()
    #     self.memory = Memory()
    #     self.ssd = SSD()

    # def start(self):
    #     # self.memory.load() # Optional
    #     self.ssd.read()
    #     self.cpu.execute()


def client():
    computer_facade = Computer(CPU, Memory)
    computer_facade.start()


client()
