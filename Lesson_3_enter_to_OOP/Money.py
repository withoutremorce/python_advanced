from decimal import Decimal


class Money:
    def __init__(self, amount, currency):
        self.amount = Decimal(amount)
        self.currency = currency

    def __str__(self):
        return '{} {}'.format(self.amount, self.currency)

    def __repr__(self): return 'Money({}, "{}")'.format(self.amount, self.currency)

    def __eq__(self, other):
        return isinstance(other, Money) and self.amount == other.amount and self.currency == other.currency

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        self._amount = amount


class Functor:
    def __call__(self):
        pass


class Counter:
    def __init__(self):
        self.x = 0
    def __call__(self):
        self.x +=1
        return self.x


sum1 = Money(10, 'UAH')
print(sum1)

sum2 = Money(10, 'USD')
sum2.amount = 20
sum2.currency = 'USD'

print(sum2)

c = Money(10, 'UAH')
print(sum1 == c)

c = Counter()

print(c())


sum2.amount

