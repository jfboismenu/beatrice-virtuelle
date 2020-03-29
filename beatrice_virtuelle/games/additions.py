from random import randint

from .base_game import BaseGame

class Additions(BaseGame):
    intent = "Additions"

    _max = 14

    @classmethod
    def ask_question(cls):
        # Pick a number between 0 and the max.
        number = randint(0, cls._max)
        # The pick another number 0 and the biggest number that when
        # addd to the first one would give the max.
        another_number = randint(0, cls._max - number)
        return ("%d, plus, %d." % (number, another_number), number + another_number)