from itertools import islice

def fac(n):
    """
    Факториал

    Факториал числа N - произведение всех целых чисел от 1 до N
    включительно. Например, факториал числа 5 - произведение
    чисел 1, 2, 3, 4, 5.

    Функция должна вернуть факториал аргумента, числа n.
    """
    number = 1
    numbers_set = set()
    for i in range(n+1):
        if i >= 1:
            numbers_set.add(i)
    print(numbers_set)
    for j in numbers_set:
        number = j * number
        print(j)
    print('number {}'.format(number))


def gcd(a, b):
    """
    Наибольший общий делитель (НОД) для двух целых чисел.

    Предполагаем, что оба аргумента - положительные числа
    Один из самых простых способов вычесления НОД - метод Эвклида,
    согласно которому

    1. НОД(a, 0) = a
    2. НОД(a, b) = НОД(b, a mod b)

    (mod - операция взятия остатка от деления, в python - оператор '%')
    """
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
    print(nod_for_a)
    print(nod_for_b)
    print(j)
    return j


def fib():
    """
    Генератор для ряда Фибоначчи

    Вам необходимо сгенерировать бесконечный ряд чисел Фибоначчи,
    в котором каждый последующий элемент ряда является суммой двух
    предыдущих. Начало последовательности: 1, 1, 2, 3, 5, 8, 13, ..

    Подсказка по реализации: для бесконечного цикла используйте идиому

    while True:
      ..

    """
    fib_numbers = list()
    fib_numbers.append(1)
    fib_numbers.append(1)
    while True:
        yield fib_numbers[-2]
        fib_num = fib_numbers[-1] + fib_numbers[-2]
        fib_numbers.append(fib_num)

def flatten(seq):
    """
    Функция, преобразующая вложенные последовательности любого уровня
    вложенности в плоские, одноуровневые.
    #
    # >>> flatten([])
    # []
    # >>> flatten([1, 2])
    # [1, 2]
    # >>> flatten([1, [2, [3]]])
    # [1, 2, 3]
    # >>> flatten([(1, 2), (3, 4)])
    # [1, 2, 3, 4]
    # """

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
    """
    Декоратор, подсчитывающий количество вызовов задекорированной функции.

    Пример использования:

    @call_count
    def add(a, b):
        return a + b
    #
    # >>> add.call_count
    # 0
    # >>> add(1, 2)
    # 3
    # >>> add.call_count
    # 1

    Подсказки по реализации: функторы, @property

    """
    # def wrapper(*args, **kwargs):
    #     wrapper.call_count += 1
    #     return property(fn(*args, **kwargs))
    # wrapper.call_count = 0
    # return wrapper

    # def __call__(self, instance):
    #     call_count =0
    #     call_count+=1
    #     return call_count

    _call_count = 0

    def __init__(self, *args, **kwargs):
        pass


    def __call__(self, *args, **kwargs):
        self._call_count += 1
        return locals()
        # a = {'args': args, 'kwargs': kwargs}
        # if args and kwargs:
        #     return a
        # elif args:
        #     return args
        # elif kwargs:
        #     return kwargs

    @property
    def call_count(self, *args, **kwargs):
        return self._call_count


    # call_count = fget
    # def fset(self, *args, **kwargs):
    #     if args is not None and kwargs is not None:
    #         return args, kwargs
    #     elif kwargs is None:
    #         return args
    #     elif args is None:
    #         return kwargs



# print(fac(5))
# print gcd(2, 4)
# f = fib()
# head = islice(fib(), 10)
# print(fib())
# assert list(head) == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# while True:
#     print(next(f))
#print(flatten(seq=[[4, [2]], 5, [6, (7, 8,[9])]]))

# @call_count
# def add(*args, **kwargs):
#     return locals()
#
# args = (1, 2)
# kwargs = {'a': 3}
# print(add(*args, **kwargs))
#
# print(add(1, 2))
# print(add.call_count)
# add(2,3)
# print(add.call_count)

@call_count
def add(a, b):
    return locals()

print('here',add.call_count)
args = (1, 2)
kwargs = {'a': 3}
add(*args, **kwargs)
print('here',add.call_count)
print(add(*args, **kwargs))
# # for i in range(101):
# #     add(1, 2)
# #     print(add.call_count)
# print(add.call_count)
# add.call_count = 1000
# print(add.call_count)