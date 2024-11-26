from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey,  DateTime, Text, Enum, Boolean
from sqlalchemy.orm import relationship
from app.database import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True) #ver si hacerlo con mapped column o column
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)

    projects_created = Column(Integer, default=0)
    projects_contributed = Column(Integer, default=0)

    projects = relationship("Project", back_populates="creator")
    contributions = relationship("Contribution", back_populates="user")