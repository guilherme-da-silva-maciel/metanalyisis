from sqlalchemy import Column,String,Integer,ForeignKey,DateTime
from sqlalchemy.orm import relationship
from core.configs import settings
from datetime import datetime

class ReviewModel(settings.DBBaseModel):

    __tablename__ = "reviews"

    id = Column(Integer,autoincrement=True,nullable=False,primary_key=True)
    movie_name = Column(String(50),nullable=False)
    reviewer_name = Column(String(50),nullable=False)
    review = Column(String(1000),nullable=False)
    created_at = Column(DateTime,default=datetime.now().strftime("%H:%M:%S"))
    updated_at = Column(DateTime,default=datetime.now().strftime("%H:%M:%S"))
    reviewer_id = Column(Integer,ForeignKey('users.id'))
    movie_id = Column(Integer,ForeignKey('movies.id'))
    reviewer = relationship("UserModel",back_populates="reviews",lazy="joined")
    movie = relationship("MovieModel",back_populates="reviews",lazy="joined")
