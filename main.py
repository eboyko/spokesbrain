from src.requests.get_answer_request import GetAnswerRequest
from src.repositories.answers_repository import AnswersRepository
from src.services.guesses_service import GuessesService
import fastapi

answers_repository = AnswersRepository("assets/answers.json")
guesser = GuessesService(answers_repository.all())
server = fastapi.FastAPI()


@server.post("/api/alpha/answers")
async def answers(request: GetAnswerRequest):
    guess = guesser.get_guess(request.question)

    return {
        "text": guess.answer.text,
        "confidence": guess.confidence,
        "traces": guess.traces
    }
