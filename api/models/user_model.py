from typing import TYPE_CHECKING
from sqlalchemy import Integer, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship, Query
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from api.database import Base
from . import BaseModel

if TYPE_CHECKING:
    from .analyst_model import Analyst
    from .customer_model import Customer


class User(Base, BaseModel):
    __allow_unmapped__ = True
    query: Query

    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    first_name: Mapped[str] = mapped_column(String(50), nullable=True)
    last_name: Mapped[str] = mapped_column(String(50), nullable=True)
    role: Mapped[int] = mapped_column(Integer, nullable=False, default=2)
    state: Mapped[int] = mapped_column(Integer, nullable=False, default=1)
    created_at: Mapped[datetime] = mapped_column(DateTime)
    updated_at: Mapped[datetime] = mapped_column(DateTime)

    analyst: Mapped["Analyst"] = relationship()
    customer: Mapped["Customer"] = relationship()

    def __init__(
        self,
        email: str,
        password: str,
        first_name: str = None,
        last_name: str = None,
    ):
        self.email = email
        self.password = generate_password_hash(password)
        self.first_name = first_name
        self.last_name = last_name
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __repr__(self) -> str:
        return "<%r>" % self.email

    def verify_password(self, password):
        return check_password_hash(self.password, password)
