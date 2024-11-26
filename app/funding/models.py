from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey,  DateTime, Text, Enum, Boolean
from sqlalchemy.orm import relationship
from app.database import Base

class Project(Base):
    __tablename__ = 'projects'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    description = Column(Text, nullable=False)
    goal_amount = Column(Float, nullable=False)
    contributions_count = Column(Integer, default=0)
    current_amount = Column(Float, default=0.0)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    status = Column(Enum("activo", "cancelled", "completed"), default="active")

    creator_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    creator = relationship("User", back_populates="projects")
    contributions = relationship("Contribution", back_populates="project")
    evaluations = relationship("Evaluation", back_populates="project")

class Contribution(Base):
    __tablename__ = 'contributions'
    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey('projects.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    amount = Column(Float, nullable=False)
    contributed_at = Column(DateTime, nullable=False)
    payment_method = Column(String, nullable=False)

    user = relationship("User", back_populates="contributions")
    project = relationship("Project", back_populates="contributions")

class Evaluation(Base):
    __tablename__ = 'evaluations'
    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey('projects.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    rating = Column(Integer, nullable=False)
    comment = Column(Text)  #este es comentario de la reseña o evaluacion :P
    created_at = Column(DateTime, nullable=False)

    user = relationship("User")
    project = relationship("Project", back_populates="evaluations")

class Comment(Base):  #esto son comentarios generales :D
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey('projects.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, nullable=False)

    user = relationship("User")
    project = relationship("Project")