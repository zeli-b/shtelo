from shtelo_economy import Currency


class Company:
    def __init__(self, discord_id: int, balance: int, currency: Currency):
        self.discord_id = discord_id
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
        self.balance -= amount
        other.balance += amount

    def get_paid_by(self, other: 'Company', amount: float):
        return other.pay_to(self, amount)
