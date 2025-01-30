from pydantic import BaseModel, EmailStr, validator
from app.utils.auth_utils import validate_password
import re
from fastapi import HTTPException

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

    @validator("email")
    def email_validator(cls, email):
        """
        Ensures email contains '@' and ends with a valid domain like .com, .net, .org
        """
        email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$"
        if not re.match(email_regex, email):
            raise HTTPException(
                status_code=400,
                detail="Invalid email format. Must be a valid email with '@' and a domain like .com, .net, .org."
            )
        return email

    @validator("password")
    def password_validator(cls, password):
        validate_password(password)
        return password

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        orm_mode = True

class QuestionCreate(BaseModel):
    question: str
    option_a: str
    option_b: str
    option_c: str
    option_d: str
    correct_answer: int

class QuestionOut(BaseModel):
    id: int
    question: str
    option_a: str
    option_b: str
    option_c: str
    option_d: str
    correct_answer: int

    class Config:
        orm_mode = True
