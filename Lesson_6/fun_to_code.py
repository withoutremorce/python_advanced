from collections import Sequence, Mapping
# dict, OrderedDict
# str, list, dict, tuple, int, float
def encode(val):
    if isinstance(val, str):
        print('str')
    elif isinstance(val, Sequence):
        print('seque')
    elif isinstance(val, Mapping):
        print('Mapping')
    else:
        raise NotImplemented

class Test:
    a =1
    def __init__(self, b):
        self.b = b

    def __getattr__(self, name):
        return  'Attribute {}'.format(name)

    def __getattribute__(self, name):
        print('Accessing attribute {}'.format(name))
        return object.__getattribute__(self,name)

    def __setattr__(self, key, value):
        raise AttributeError

    def __delattr__(self, item):
        pass