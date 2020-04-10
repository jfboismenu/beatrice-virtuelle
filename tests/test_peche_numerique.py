import pytest
from beatrice_virtuelle.games import peche_numerique


@pytest.mark.parametrize(
    "scale,template_index,base,to_add,expected_question,expected_answer",
    [
        (1, 0, 100, 3, "3 unité de plus que 100.", 103),
        (1, 1, 100, 3, "Ajoute 3 unité à 100.", 103),
        (1, 2, 100, 3, "Additionne 3 unité et 100.", 103),
        (10, 0, 100, 3, "3 dizaine de plus que 100.", 130),
        (10, 1, 100, 3, "Ajoute 3 dizaine à 100.", 130),
        (10, 2, 100, 3, "Additionne 3 dizaine et 100.", 130),
        (100, 0, 100, 3, "3 centaine de plus que 100.", 400),
        (100, 1, 100, 3, "Ajoute 3 centaine à 100.", 400),
        (100, 2, 100, 3, "Additionne 3 centaine et 100.", 400),
    ],
)
def test_digit_func(
    scale, template_index, base, to_add, expected_question, expected_answer
):
    question, answer = peche_numerique.digit_func(
        scale, peche_numerique._add_units_questions[template_index], base, to_add
    )
    assert question == expected_question
    assert answer == expected_answer
