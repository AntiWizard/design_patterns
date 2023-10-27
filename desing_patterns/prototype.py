"""
    - Prototype is a creational design pattern that lets you copy existing objects
    without making your code dependent on their classes.
"""

import copy


class Prototype:
    def __init__(self):
        self.objects = {}

    def register(self, name, obj):
        self.objects[name] = obj

    def unregister(self, name):
        del self.objects[name]

    def clone(self, name, **kwargs):
        cloned_obj = copy.deepcopy(self.objects.get(name))
        cloned_obj.__dict__.update(kwargs)
        return cloned_obj


def client(name, obj, **kwargs):
    prototype = Prototype()
    prototype.register(name, obj)
    return prototype.clone(name, **kwargs)


# example

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person = Person('john', 34)

p_clone = client('ex1', person, age=20)  # update age from 34 to 20
p_clone_clone = client('ex1', p_clone, age=18)  # clone from cloned

print(p_clone.__dict__)
print(p_clone.age == 20)
print(id(person.name) == id(p_clone.name))  # True (for age will be False 34 != 20)
