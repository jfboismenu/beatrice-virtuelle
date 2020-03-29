from random import randint

from .base_game import BaseGame

def number_between():
    answer = randint(10, 1000)
    return (
        "Quel est le nombre entre %d et %d" % (answer - 1, answer + 1),
        answer
    )

def number_before():
    answer = randint(10, 1000)
    return (
        "Quel est le nombre avant %s?" % (answer + 1),
        answer
    )

def number_after():
    answer = randint(10, 1000)
    return (
        "Quel est le nombre après %s?" % (answer - 1),
        answer
    )

def _pick_one_of(posibilities):
    return posibilities[randint(0, len(posibilities) - 1)]

_add_units_questions = (
    "{{to_add}} {scale_name} de plus que {{base}}.",
    "Ajoute {{to_add}} {scale_name} à {{base}}.",
    "Additionne {{to_add}} {scale_name} et {{base}}."
)

def _scale_to_word(scale):
    return {
        1: "unité",
        10: "dizaine",
        100: "centaine"
    }[scale]

def digit_func(scale, template, base, to_add):
    template_with_scale = template.format(scale_name=_scale_to_word(scale))
    question = template_with_scale.format(to_add=to_add, base=base)
    answer = to_add * scale + base
    return (question, answer)

def add_digit_func():
    base = randint(10, 1000)
    scale = _pick_one_of([1, 10, 100])
    to_add = randint(1, 9)
    question = _pick_one_of(_add_units_questions)
    return digit_func(scale, question, base, to_add)
 

class PecheNumerique(BaseGame):
    intent = "PecheNumerique"

    _question_types = number_between, number_after, number_before, add_digit_func

    @classmethod
    def ask_question(cls):
        return _pick_one_of(cls._question_types)()