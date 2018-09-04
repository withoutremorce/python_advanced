class Money:
    def __init__(self, currency):
        self._currency = currency
        self._amount = None

    def __get__(self, obj, owner):
        return self._amount

    def __set__(self, obj, amount):
        self._amount = amount

    # @property
    # def currency(self):
    #     return self._currency


class Account:
    primary = Money('UAH')
    bonus = Money('UAH')


a = Account()
a.primary = 100