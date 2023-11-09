from sqlalchemy import ForeignKey, Integer, String, DateTime, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship, Query
from datetime import datetime
from api.database import Base
from api.models.user_model import User
from api.models.payment_method_model import PaymentMethod
from . import BaseModel


class Customer(Base, BaseModel):
    __allow_unmapped__ = True
    query: Query

    __tablename__ = "customers"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    country: Mapped[int] = mapped_column(Integer, nullable=False)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    employe_number: Mapped[int] = mapped_column(Integer)
    sector: Mapped[str] = mapped_column(String(50))
    areas: Mapped[str] = mapped_column(String(255))
    platforms: Mapped[str] = mapped_column(String(255))
    payment_method_id: Mapped[int] = mapped_column(ForeignKey("payment_methods.id"))
    invoice_required: Mapped[bool] = mapped_column(Boolean)
    ruc: Mapped[str] = mapped_column(String(12))
    address: Mapped[str] = mapped_column(String(255))
    profile_image_url: Mapped[str] = mapped_column(String(255), nullable=True)
    banner_image_url: Mapped[str] = mapped_column(String(255), nullable=True)
    state: Mapped[int] = mapped_column(Integer, nullable=False, default=1)
    created_at: Mapped[datetime] = mapped_column(DateTime)
    updated_at: Mapped[datetime] = mapped_column(DateTime)

    payment_method: Mapped["PaymentMethod"] = relationship(lazy="joined")
    # user: Mapped["User"] = relationship(back_populates="customer")

    def __init__(
        self,
        user: User,
        country: int,
        name: str,
        employe_number: str = None,
        sector: str = None,
        areas: str = None,
        platforms: str = None,
        payment_method: PaymentMethod = None,
        invoice_required: Boolean = None,
        ruc: str = None,
        address: str = None,
        profile_image_url: str = None,
        banner_image_url: str = None,
    ):
        self.user_id = user.id
        self.country = country
        self.name = name
        self.employe_number = employe_number
        self.sector = sector
        self.areas = areas
        self.platforms = platforms
        self.payment_method_id = payment_method.id
        self.invoice_required = invoice_required
        self.ruc = ruc
        self.address = address
        self.profile_image_url = profile_image_url
        self.banner_image_url = banner_image_url
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __repr__(self) -> str:
        return "<%r>" % self.name
