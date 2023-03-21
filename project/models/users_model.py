from sqlalchemy import Column,String,Integer,ForeignKey,DateTime
from datetime import datetime
from sqlalchemy.orm import relationship
from core.configs import settings

class UserModel(settings.DBBaseModel):
    __tablename__ = 'users'
    id = Column(Integer,autoincrement=True,nullable=False,primary_key=True,unique=True)
    username = Column(String(50),unique=True,nullable=False)
    name = Column(String(50),nullable=False)
    surname = Column(String(50),nullable=True)
    created_at = Column(DateTime,default=datetime.now().strftime("%H:%M:%S"))
    email = Column(String(35),nullable=False,unique=True)
    password = Column(String(50),nullable=False)
    uid = Column(String(50),nullable=False)
    reviews = relationship("ReviewModel",cascade="all, delete-orphan",back_populates="reviewer",lazy="joined")
    permissions = relationship("RuleModel",cascade="all, delete-orphan",back_populates="user",lazy="joined")
