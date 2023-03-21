from sqlalchemy import Column,String,Integer,ForeignKey,DateTime
from sqlalchemy.orm import relationship
from core.configs import settings
from datetime import datetime

class MovieModel(settings.DBBaseModel):
    
    __tablename__ = "movies"

    id = Column(Integer,autoincrement=True,nullable=False,primary_key=True)
    name = Column(String(110),nullable=False)
    average_score = Column(Integer,nullable=False)
    description = Column(String(500),nullable=False)
    year = Column(Integer,nullable=False)
    awards = Column(String(150),nullable=False)
    director = Column(String(45),nullable=False)
    review = relationship("ReviewModel",back_populates="movies",lazy="joined")

