from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from app.main.database import get_db
from app.main.models import Question
from app.main.schemas import QuestionCreate, QuestionOut
from app.services.question_service import QuestionService

class QuestionController:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db
        self.question_service = QuestionService()

    def get_all_questions(self) -> list[QuestionOut]:
        """
        Retrieves all quiz questions.
        """
        return self.question_service.get_all_questions(self.db)

    def create_question(self, question: QuestionCreate) -> QuestionOut:
        """
        Creates a new quiz question.
        """
        return self.question_service.create_question(self.db, question)
