# Задание 1. Встроенные типы данных, операторы, функции и генераторы
#
# Напишите реализации объявленных ниже функций. Для проверки
# корректности реализации ваших функций, запустите тесты:
#
# pytest test_homework01.py
#
# Если написанный вами код не содержит синтаксических ошибок,
# вы увидите результаты тестов ваших решений.


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
    for j in numbers_set:
        number = j * number
    return number


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
        fib_num = fib_numbers[-1] + fib_numbers[-2]
        fib_numbers.append(fib_num)
        yield fib_numbers


def flatten(seq):
    """
    Функция, преобразующая вложенные последовательности любого уровня
    вложенности в плоские, одноуровневые.

    >>> flatten([])
    []
    >>> flatten([1, 2])
    [1, 2]
    >>> flatten([1, [2, [3]]])
    [1, 2, 3]
    >>> flatten([(1, 2), (3, 4)])
    [1, 2, 3, 4]
    """
    temp = list()
    for i in seq:
        if type(i) is list or type(i) is tuple:
            print('true')
            temp.extend(flatten(i))
        else:
            temp.append(i)
            print('i = {}'.format(i))
    return temp


def call_count(fn):
    """
    Декоратор, подсчитывающий количество вызовов задекорированной функции.

    Пример использования:

    @call_count
    def add(a, b):
        return a + b

    >>> add.call_count
    0
    >>> add(1, 2)
    3
    >>> add.call_count
    1

    Подсказки по реализации: функторы, @property

    """
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        return fn(*args, **kwargs)
    wrapper.call_count = 0
    return wrapper
