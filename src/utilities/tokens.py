from string import punctuation

from nltk import word_tokenize
from nltk.corpus import stopwords

from src.models.token import Token


def is_word_processable(word) -> bool:
    """
    Describes conditions when the given word can be processed.
    """

    return word not in stopwords.words('russian') and word not in punctuation


def get_tokens(sentence):
    """
    Returns the keywords of the given sentence.
    """

    return [Token(keyword) for keyword in word_tokenize(sentence.lower()) if is_word_processable(keyword)]
