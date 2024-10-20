from typing import Optional
from sqlmodel import SQLModel, Field
from . import restart_db


class Pizza(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    price: int
    summary: str




#EOF

restart_db()