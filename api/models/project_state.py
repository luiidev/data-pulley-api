from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from api.database import Base


class ProjectState(Base):
    __tablename__ = "project_states"
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    state = Column(Integer, nullable=False, default=1)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    
    def __init__(self, name: String):
        self.name = name
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        
    def __repr__(self) -> str:
        return "<%r>" % self.name