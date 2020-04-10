# -*- coding: utf-8 -*-
# Unlicense
#
# See LICENSE at the root of this project for more info.


class BaseGame:
    @classmethod
    def handle_answer(cls, given, expected):
        if expected != given:
            response = f"Désolé, la réponse était {expected}."
        else:
            response = "Bonne réponse!"

        return response
