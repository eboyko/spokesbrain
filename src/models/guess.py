from gensim.models.keyedvectors import load_word2vec_format

vectors_repository = load_word2vec_format("assets/ruwikiruscorpora.bin", binary=True)


def get_similarity(one, another):
    """
    Returns the similarity of two words.
    """

    return vectors_repository.similarity(one, another)


class Guess:
    """
    Describes a guess about an answer similarity to a question.
    """

    class Trace:
        """
        Wrapper for guessing process trace.
        """

        def __init__(self, topic):
            self.topic = topic
            self.confidence = 0.0
            self.keywords = []
            self.errors = []

    def __init__(self, answer, keywords):
        self.answer = answer
        self.confidence = 0.0
        self.traces = []

        if len(answer.topics) == 0:
            return

        for topic in answer.topics:
            trace = Guess.Trace(topic)
            self.traces.append(trace)

            for keyword in keywords:
                try:
                    similarity = get_similarity(
                        f'{topic.normal_form}_{topic.part_of_speech}',
                        f'{keyword.normal_form}_{keyword.part_of_speech}'
                    )

                    trace.confidence += similarity
                    trace.keywords.append({"keyword": keyword, "similarity": f'{similarity:.2f}'})

                except KeyError:
                    trace.errors.append(f'{topic.normal_form} × {keyword.normal_form}')

        self.confidence = sum([trace.confidence for trace in self.traces]) / len(self.traces)
