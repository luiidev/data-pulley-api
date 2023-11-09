from sqlalchemy import ForeignKey, Integer, String, DateTime, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from api.database import Base
from api.models.analyst_model import Analyst
from api.models.customer_model import Customer
from api.models.payment_state_model import PaymentState
from api.models.project_proposal_model import ProjectProposal
from api.models.project_state import ProjectState


class Project(Base):
    __tablename__ = "projects"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    customer_id: Mapped[int] = mapped_column(Integer, ForeignKey("customers.id"))
    analyst_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("analysts.id"), nullable=True
    )
    project_proposal_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("project_proposals.id"), nullable=True
    )
    name: Mapped[str] = mapped_column(String(255))
    detail: Mapped[str] = mapped_column(Text)
    platforms: Mapped[str] = mapped_column(String(255), nullable=True)
    tools: Mapped[str] = mapped_column(String(255), nullable=True)
    image_url: Mapped[str] = mapped_column(String(255), nullable=True)
    project_url: Mapped[str] = mapped_column(String(255), nullable=True)
    progress_status: Mapped[int] = mapped_column(Integer)
    payment_state_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("payment_states.id")
    )
    project_state_id: Mapped[int] = mapped_column(Integer, default=1)
    created_at: Mapped[datetime] = mapped_column(DateTime)
    updated_at: Mapped[datetime] = mapped_column(DateTime)

    # state: Mapped["ProjectState"] = relationship()

    def __init__(
        self,
        customer: Customer,
        name: str,
        detail: str,
        project_state: ProjectState,
        payment_state: PaymentState,
        analyst: Analyst = None,
        project_proposal: ProjectProposal = None,
        platforms: str = None,
        tools: str = None,
        image_url: str = None,
        project_url: str = None,
        progress_status: int = None,
    ):
        self.customer_id = customer.id
        self.payment_state_id = payment_state.id
        self.project_state_id = project_state.id
        self.name = name
        self.detail = detail
        self.platforms = platforms
        self.tools = tools
        self.image_url = image_url
        self.project_url = project_url
        self.progress_status = progress_status
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if analyst:
            self.analyst_id = analyst.id
        if project_proposal:
            self.project_proposal_id = project_proposal.id

    def __repr__(self) -> str:
        return "<%r>" % self.name
