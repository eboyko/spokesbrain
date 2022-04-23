import pydantic


class GetAnswerRequest(pydantic.BaseModel):
    """
    Describes the question request body.
    """
    question: str
