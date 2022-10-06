from math import exp, log

from economy.const import ELIT_SYMBOL


def symbolize(elit: float, format_string: str = ',.2f') -> str:
    return f'{format(elit, format_string)} {ELIT_SYMBOL}'


class Currency:
    def __init__(self, name: str, symbol: str, total_currency: float, total_value: float, rotating: float):
        self.name = name
        self.symbol = symbol
        self.total_currency = total_currency
        self.total_value = total_value
        self.rotating = rotating

    def __str__(self) -> str:
        return f'{self.name}({self.symbol})'

    def get_expectation(self) -> float:
        return self.total_value / (self.total_currency - self.rotating)

    def get_frozen(self) -> float:
        return self.total_currency - self.rotating

    def symbolize(self, amount: float, format_string: str = ',.2f') -> str:
        """ Returns formatted ``amount`` with currency symbol. """
        return f'{format(amount, format_string)} {self.symbol}'

    def symbolize_expectation(self, expectation: float, format_string: str = ',.2f') -> str:
        """ Returns formatted ``expectation`` with currency per elit symbol. """
        return f'{format(expectation, format_string)} {ELIT_SYMBOL}/{self.symbol}'

    def rotate(self, elit: float) -> float:
        """
        Rotate ``elit`` amount of Elit into rotation.

        :return: ``elit`` in currency
        """

        if elit > self.total_value:
            raise ValueError(f'Cannot rotate more than the total value. '
                             f'Current total value is {symbolize(self.total_value)} '
                             f'and trying to rotate {symbolize(elit)}')

        delta_frozen = self.get_frozen() * (exp(elit / self.total_value) - 1)
        self.rotating += delta_frozen
        return delta_frozen

    def freeze(self, amount: float) -> float:
        """
        Freeze ``amount`` amount of currencies into frozen.

        :return: ``amount`` in Elit
        """

        if amount > self.rotating:
            raise ValueError(f'Cannot freeze more than the rotating. '
                             f'Current rotating is {self.symbolize(self.rotating)} '
                             f'and trying to freeze {self.symbolize(amount)}')

        absolute_value = self.total_value * log(amount / self.get_frozen() + 1)
        self.rotating -= amount
        return absolute_value
