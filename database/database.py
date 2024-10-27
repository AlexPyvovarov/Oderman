from typing import Optional
from sqlmodel import SQLModel, Field, Relationship
from . import restart_db


class Pizza(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    price: int
    summary: str


class Option(SQLModel, table = True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(unique=True)
    question_id: int = Field(foreign_key="question.id")


class Question(SQLModel, table = True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(unique=True)
    options: list["Option"]= Relationship()


class Vote(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    question_id: int = Field(foreign_key="question.id")
    option_id: int = Field(foreign_key="option.id")
    question: Question = Relationship()
    option: Option = Relationship()



#EOF

restart_db()