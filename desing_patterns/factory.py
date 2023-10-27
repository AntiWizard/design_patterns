"""
    - Factory is a creational design pattern that provide an interface for creating objects
    in a superclass, but allows subclasses to alter the type of objects that will be created.

"""

from abc import ABC, abstractmethod


class File(ABC):
    def __init__(self, file):
        self.file = file

    @abstractmethod
    def make(self):
        pass

    def call_edit(self):
        product = self.make()
        result = product.edit(self.file)
        return result


class JsonFile(File):
    def make(self):
        return Json()


class XmlFile(File):
    def make(self):
        return Xml()


class Json:
    def edit(self, file):
        return f'Working on {file} Json...!'


class Xml:
    def edit(self, file):
        return f'Working on {file} Xml...!'


def client(file, format_):
    formats = {
        'json': JsonFile,
        'xml': XmlFile
    }

    result = formats[format_](file)
    return result.call_edit()


print(client('example', 'json'))
print(client('example', 'xml'))
