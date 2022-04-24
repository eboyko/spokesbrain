from src.models.token import Token


class Answer:
    """
    Describes model of a single Spokesbot' answer.
    There is no methods here. Now it is just a data wrapper.
    """

    def __init__(self, text, topics):
        self.text = text
        self.topics = [Token(topic) for topic in topics]
