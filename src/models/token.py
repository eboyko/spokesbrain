from src.utilities.morphology import get_morpheme


class Token:
    """
    Represents an original word with morphological information.
    """

    def __init__(self, word):
        self.word = word

        morpheme = get_morpheme(word)
        self.normal_form = morpheme.normal_form
        self.part_of_speech = morpheme.tag.POS

    def __str__(self):
        return self.word
