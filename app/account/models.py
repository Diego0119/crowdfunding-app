from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey, DateTime, Text, Enum, Boolean
from sqlalchemy.orm import relationship,  Mapped, mapped_column
from app.database import Base
import sqlalchemy as sa
from typing import TYPE_CHECKING, Optional, List

if TYPE_CHECKING:
    from app.funding.models import Project, Contribution, Evaluation, Comment

class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String, unique=True, index=True)
    email: Mapped[str] = mapped_column(String, unique=True, index=True)
    password: Mapped[Optional[str]] = mapped_column(String)
    money = sa.Column(sa.Float, nullable=False, default=0.0) 
    
    projects_created: Mapped[int] = mapped_column(default=0)
    projects_contributed: Mapped[int] = mapped_column(default=0)
    
    projects: Mapped[List["Project"]] = relationship("Project", back_populates="creator")
    contributions: Mapped[List["Contribution"]] = relationship("Contribution", back_populates="user")