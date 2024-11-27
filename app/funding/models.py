from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey, DateTime, Text, Enum, Boolean
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.database import Base
from typing import TYPE_CHECKING, Optional, List
from datetime import datetime

if TYPE_CHECKING:
    from app.account.models import User

class Project(Base):
    __tablename__ = 'projects'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, index=True, nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    goal_amount: Mapped[float] = mapped_column(nullable=False)
    contributions_count: Mapped[int] = mapped_column(default=0)
    current_amount: Mapped[float] = mapped_column(default=0.0)
    start_date: Mapped[datetime] = mapped_column(DateTime, nullable=False)  # Cambiado
    end_date: Mapped[datetime] = mapped_column(DateTime, nullable=False)    # Cambiado
    status: Mapped[str] = mapped_column(Enum("active", "cancelled", "completed"), default="active")

    creator_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=False)

    creator: Mapped["User"] = relationship("User", back_populates="projects")
    contributions: Mapped[List["Contribution"]] = relationship("Contribution", back_populates="project")
    evaluations: Mapped[List["Evaluation"]] = relationship("Evaluation", back_populates="project")

class Contribution(Base):
    __tablename__ = 'contributions'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    project_id: Mapped[int] = mapped_column(ForeignKey('projects.id'), nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=False)
    amount: Mapped[float] = mapped_column(nullable=False)
    contributed_at: Mapped[datetime] = mapped_column(nullable=False)
    payment_method: Mapped[str] = mapped_column(String, nullable=False)

    user: Mapped["User"] = relationship("User", back_populates="contributions")
    project: Mapped["Project"] = relationship("Project", back_populates="contributions")

class Evaluation(Base):
    __tablename__ = 'evaluations'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    project_id: Mapped[int] = mapped_column(ForeignKey('projects.id'), nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=False)
    rating: Mapped[int] = mapped_column(nullable=False)
    comment: Mapped[Optional[str]] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(nullable=False)


    user: Mapped["User"] = relationship("User")
    project: Mapped["Project"] = relationship("Project", back_populates="evaluations")

class Comment(Base):
    __tablename__ = 'comments'
    
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    project_id: Mapped[int] = mapped_column(ForeignKey('projects.id'), nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[DateTime] = mapped_column(nullable=False)

    user: Mapped["User"] = relationship("User")
    project: Mapped["Project"] = relationship("Project")
