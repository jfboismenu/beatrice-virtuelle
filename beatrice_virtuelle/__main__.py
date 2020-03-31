import logging
from flask import Flask, render_template
from flask_ask import Ask, question, session

from beatrice_virtuelle.games import PecheNumerique, Additions

app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger("flask_ask").setLevel(logging.DEBUG)

@ask.launch
def new_game():
    return question("Bienvenue dans la classe virtuelle de Béatrice. À quel jeu veux-tu jouer?")

games = {
    PecheNumerique.intent: PecheNumerique,
    Additions.intent: Additions
}

def register_game_intent(name, handler):
    @ask.intent(name + "Intent")
    def start_game():
        session.attributes['game'] = name
        next_question, next_answer = handler.ask_question()
        session.attributes['question'] = next_question
        session.attributes['answer'] = next_answer
        return question(next_question)


@ask.intent("SingleNumberAnswerIntent", convert={'answer': int})
def handle_answer(answer):
    # FIXME: handle game not in attributes.
    # Find which game we are playing.
    handler = games[session.attributes["game"]]

    if answer == "?":
        return question(
            " ".join(
                [
                    "Désolé, pourrais-tu répéter?",
                    session.attributes["question"]
                ]
            )
        )

    expected_answer = session.attributes["answer"]

    print(answer, type(answer), expected_answer)
    result = handler.handle_answer(
        answer, expected_answer
    )
    next_question, next_answer = handler.ask_question()

    session.attributes["answer"] = next_answer
    return question(
        " ".join([
            result,
            "Prochaine question.",
            next_question
        ])
    )

# Register all the game handlers.
for name, handler in games.items():
    register_game_intent(name, handler)

if __name__ == '__main__':
    app.run(debug=True, port=5000)


