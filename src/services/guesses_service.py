from random import randint

from src.models.guess import Guess
from src.utilities.tokens import get_tokens


class GuessesService:
    """
    Describes comparison procedure between Spokesbot' answers and user' question.
    """

    GUESS_CONFIDENCE_THRESHOLD = 0.0

    def __init__(self, answers):
        self.answers = answers

    def get_guess(self, question):
        keywords = get_tokens(question)

        guesses = []

        for answer in self.answers:
            guesses.append(Guess(answer, keywords))

        guesses.sort(key=lambda guess: guess.confidence, reverse=True)

        if guesses[0].confidence > self.GUESS_CONFIDENCE_THRESHOLD:
            return guesses[0]
        else:
            return guesses[randint(0, len(guesses))]
