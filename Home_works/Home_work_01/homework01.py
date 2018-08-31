def fac(n):
    number = 1
    numbers_set = set()
    for i in range(n+1):
        if i >= 1:
            numbers_set.add(i)
    for j in numbers_set:
        number = j * number
    return number


def gcd(a, b):
    j = 1
    nod_for_a = set()
    nod_for_b = set()
    for i in range(a+1):
        if a != 0 and i != 0 and a % i == 0:
            nod_for_a.add(i)
        if b != 0 and i != 0 and b % i == 0:
            nod_for_b.add(i)
    if a > b:
        for i in nod_for_a:
            if i in nod_for_b:
                j = i
    else:
        for i in nod_for_b:
            if i in nod_for_a:
                j = i
    return j


def fib():
    fib_numbers = list()
    fib_numbers.append(1)
    fib_numbers.append(1)
    while True:
        yield fib_numbers[-2]
        fib_num = fib_numbers[-1] + fib_numbers[-2]
        fib_numbers.append(fib_num)


def flatten(seq):
    temp = list()
    for i in seq:
        if type(i) is list or type(i) is tuple:
            print('true')
            temp.extend(flatten(i))
        else:
            temp.append(i)
            print('i = {}'.format(i))
    return temp


class call_count:
    def __init__(self, *args, **kwargs):
        self._call_count = 0

    def __call__(self, *args, **kwargs):
        self._call_count += 1
        return {'args': args, 'kwargs': kwargs}

    @property
    def call_count(self, *args, **kwargs):
        return self._call_count

