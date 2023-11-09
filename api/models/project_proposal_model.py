from sqlalchemy import ForeignKey, Integer, Float, Text, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from api.database import Base
from api.models.analyst_model import Analyst


class ProjectProposal(Base):
    __tablename__ = "project_proposals"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    analyst_id: Mapped[int] = mapped_column(Integer, ForeignKey("analysts.id"))
    estimated_hours: Mapped[int] = mapped_column(Integer, nullable=False)
    cost_hour: Mapped[float] = mapped_column(Float(10, 2), nullable=False)
    detail_scope: Mapped[str] = mapped_column(Text, nullable=False)
    state: Mapped[int] = mapped_column(Integer, nullable=False, default=1)
    created_at: Mapped[datetime] = mapped_column(DateTime)
    updated_at: Mapped[datetime] = mapped_column(DateTime)

    def __init__(
        self,
        analyst: Analyst,
        estimated_hours: int,
        cost_hour: float,
        detail_scope: str,
    ):
        self.analyst_id = analyst.id
        self.estimated_hours = estimated_hours
        self.cost_hour = cost_hour
        self.detail_scope = detail_scope
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __repr__(self) -> str:
        return "<%r>" % self.detail_scope