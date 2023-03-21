from sqlalchemy import Column,String,Integer,ForeignKey
from sqlalchemy.orm import relationship
from core.configs import settings

class RuleModel(settings.DBBaseModel):
    __tablename__ = "rule"
    id = Column(Integer,primary_key=True,autoincrement=True,nullable=True)
    access_type = Column(String(20),nullable=False)
    user_permission = relationship("UserRoleModel",back_populates="rule",lazy="joined")
