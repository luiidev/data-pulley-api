from sqlalchemy import ForeignKey, Integer, Float, String, DateTime, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship, Query
from datetime import datetime
from api.database import Base
from api.models.user_model import User
from api.models.payment_method_model import PaymentMethod
from . import BaseModel


class Analyst(Base, BaseModel):
    __allow_unmapped__ = True
    query: Query

    __tablename__ = "analysts"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    country: Mapped[int] = mapped_column(Integer, nullable=False)
    years_experience: Mapped[int] = mapped_column(Integer, nullable=False)
    cost_hour: Mapped[float] = mapped_column(Float(10, 2), nullable=False)
    tools: Mapped[str] = mapped_column(String(255))
    about: Mapped[str] = mapped_column(Text)
    profile_image_url: Mapped[str] = mapped_column(String(255), nullable=True)
    banner_image_url: Mapped[str] = mapped_column(String(255), nullable=True)
    payment_method_id: Mapped[int] = mapped_column(ForeignKey("payment_methods.id"))
    state: Mapped[int] = mapped_column(Integer, nullable=False, default=1)
    created_at: Mapped[datetime] = mapped_column(DateTime)
    updated_at: Mapped[datetime] = mapped_column(DateTime)

    payment_method: Mapped["PaymentMethod"] = relationship(lazy="joined")
    # user: Mapped["User"] = relationship(back_populates="analyst")

    def __init__(
        self,
        user: User,
        payment_method: PaymentMethod,
        country: str,
        years_experience: int,
        cost_hour: float,
        tools: str = None,
        about: str = None,
        profile_image_url: str = None,
        banner_image_url: str = None,
    ):
        self.user_id = user.id
        self.payment_method_id = payment_method.id
        self.country = country
        self.years_experience = years_experience
        self.cost_hour = cost_hour
        self.tools = tools
        self.about = about
        self.profile_image_url = profile_image_url
        self.banner_image_url = banner_image_url
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __repr__(self):
        return "<%r>" % self.user_id
