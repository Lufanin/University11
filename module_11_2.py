from inspect import getmodule


def  introspection_info(obj):
    return {
        'type': type(obj).__name__,
        'attributes': obj.__dict__,
        'methods': dir(obj),
        'module': getmodule(obj).__name__
    }

class MyClass:

    def __init__(self):
        self.name = 'MyClass'
        self.value = 100
        self.private_attribute = 'private'

obj = MyClass()



number_info = introspection_info(obj)
print(number_info)