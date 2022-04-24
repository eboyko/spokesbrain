from pymorphy2 import MorphAnalyzer

morphology_analyser = MorphAnalyzer()


def get_morpheme(word):
    """
    Returns the morpheme of the given word.
    """

    return morphology_analyser.parse(word)[0]
