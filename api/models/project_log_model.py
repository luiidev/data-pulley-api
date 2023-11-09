from sqlalchemy import Column, ForeignKey, Integer, Text, DateTime
from api.database import Base


class ProjectLog(Base):
    __tablename__ = "project_logs"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    log = Column(Text, nullable=False)
    state = Column(Integer, nullable=False, default=1)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)