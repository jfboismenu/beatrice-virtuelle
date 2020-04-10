# -*- coding: utf-8 -*-
# Unlicense
#
# See LICENSE at the root of this project for more info.

from random import randint

from .base_game import BaseGame


class Additions(BaseGame):
    intent = "Additions"

    _max = 20

    @classmethod
    def ask_question(cls):
        # Pick a number between 0 and the max.
        number = randint(0, cls._max)
        # The pick another number 0 and the biggest number that when
        # addd to the first one would give the max.
        another_number = randint(0, cls._max - number)
        return (f"{number}, plus, {another_number}.", number + another_number)
