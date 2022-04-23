import json

from src.models.answer import Answer


class AnswersRepository:
    """
    Describes storage actions across Spokesbot' answers.
    There is no database in the current release. All the data stores in JSON file.
    """

    def __init__(self, file_path):
        """
        Describes initial processing of the answers source file.
        :param file_path: answers file path
        """

        self.__answers = []

        with open(file_path, 'r') as data:
            for datum in json.load(data):
                self.__answers.append(Answer(datum["text"], datum["topics"]))

    def all(self) -> [Answer]:
        return self.__answers
