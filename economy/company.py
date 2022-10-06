from economy import Currency


class Company:
    def __init__(self, id_: int, balance: int, currency: Currency):
        self.id = id_
        self.balance = balance
        self.currency = currency

    def earn(self, elit: float) -> float:
        """
        Rotate ``elit`` Elit and give it to ``self``.

        :return: ``elit`` in currency
        """

        amount = self.currency.rotate(elit)
        self.balance += amount
        return amount

    def pay(self, amount: float) -> float:
        """
        Freeze ``amount`` of currency and make ``self`` pay it out

        :return: ``amount`` in Elit
        """

        elit = self.currency.freeze(amount)
        self.balance -= amount
        return elit

    def pay_to(self, other: 'Company', amount: float):
        if amount > self.balance:
            raise ValueError(f'Cannot pay more than they have. '
                             f'``self`` only have {self.currency.symbolize(self.balance)} and '
                             f'trying to pay {self.currency.symbolize(amount)}. '
                             f'(``self.id``={self.id}, ``other.id``={other.id})')

        if self.currency == other.currency:
            self.balance -= amount
            other.balance += amount
            return amount * self.currency.get_expectation()

        elit = self.pay(amount)
        other.earn(elit)
        return elit

    def get_paid_by(self, other: 'Company', amount: float):
        """ Get paid by ``other``. ``amount`` is in currency of ``self`` """
        if self.currency != other.currency:
            amount *= other.currency.get_exchange_rate_to(self.currency)
        return other.pay_to(self, amount)

    def get_balance_in_elit(self):
        return self.balance * self.currency.get_expectation()
