class BaseGame:
    @classmethod
    def handle_answer(cls, given, expected):
        if expected != given:
            response = "Désolé, la réponse était %d." % expected
        else:
            response = "Bonne réponse!"

        return response