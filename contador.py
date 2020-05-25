import pandas as pd
from random import choice
import arrow
import colorama

try:
    if get_ipython().__class__.__name__ != 'ZMQInteractiveShell':
        colorama.init()
except NameError:
    colorama.init()

colors = {'red': '\x1b[31m',
          'green': '\x1b[32m',
          'yellow': '\x1b[33m',
          'blue': '\x1b[34m',
          'magenta': '\x1b[35m',
          'cyan': '\x1b[36m',
          'light_gray': '\x1b[37m',
          'dark_gray': '\x1b[90m',
          'light_red': '\x1b[91m',
          'light_green': '\x1b[92m',
          'light_yellow': '\x1b[93m',
          'light_blue': '\x1b[94m',
          'light_magenta': '\x1b[95m',
          'light_cyan': '\x1b[96m',
          'white': '\x1b[97m',
          }


def color(string, color_name="red"):
    """Imprimir con el color especificado o rojo por defecto"""
    col = colors.get(color_name, '\x1b[31m')
    return f"{col}{string}\x1b[0m"


def no_ms(date):
    """Devuelve como string, un arrow sin los milisegundos 01:23:45 no 01:23:45.6789"""
    return str(date).split('.')[0]


class Contador:
    def __init__(self, name, total, each=1000, print_bool=True, print_color=False, color_name="red"):
        self.i = 0
        self.name = name
        self.each = each
        self.print_bool = print_bool
        self.zero = arrow.utcnow()

        if type(total) is int:
            self.total = total
        elif type(total) is pd.DataFrame:
            self.total = total.shape[0]

        self.print_color = print_color

        if color_name.lower() == "rand":
            self.color_name = choice(list(colors.keys()))
        else:
            self.color_name = color_name.lower()

    def __str__(self):
        now = arrow.utcnow()
        dif = now - self.zero
        if self.i == 0:
            each = dif / (self.i + 1)
        else:
            each = dif / self.i
        string = f"{self.name}: {self.i}/{self.total} {round(self.i / self.total * 100, 2)}%\tTimeFromZero: {no_ms(dif)}\tEachIter: {each}\tAproxLeft: {no_ms(each * (self.total - self.i))} "
        if self.print_color:
            return color(string, self.color_name)
        return string

    def __repr__(self):
        return self.__str__()

    def inc(self):
        """Incrementa el contador y si se ha habilitado el imprimir y estás en el múltiplo lo imprime"""
        self.i += 1
        if (self.i % self.each == 0 or self.i == self.total) and self.print_bool:
            print(self)

    def reset_time_zero(self):
        self.zero = arrow.utcnow()

    @staticmethod
    def print(st, color_="red"):
        """Imprime un string en un color"""
        if color_.lower() == "rand":
            color_ = choice(list(colors.keys()))
        print(color(st, color_.lower()))

    @staticmethod
    def list_colors():
        return list(colors.keys())

    @classmethod
    def pretty_list_colors(cls):
        """Imprime la lista de colores pero cada uno con su color"""
        list_ = cls.list_colors()
        for col in list_:
            cls.print(col, col)
