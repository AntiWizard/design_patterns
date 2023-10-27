"""
    Ensure they only have one instance
    Provide easy access to that instance
    Control their instantiation
"""


class Singleton(type):
    _instance = None

    def __call__(self, *args, **kwargs):
        if self._instance is None:
            self._instance = super(Singleton, self).__call__(*args, **kwargs)
        return self._instance


class Example(metaclass=Singleton):
    pass


first_instance = Example()

second_instance = Example()

print(id(first_instance) == id(second_instance))  # True
print(first_instance == second_instance and first_instance is second_instance)  # True
