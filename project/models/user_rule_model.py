from sqlalchemy import Column,Integer,ForeignKey,String
from sqlalchemy.orm import relationship
from core.configs import settings

class UserRoleModel(settings.DBBaseModel):
    __tablename__ = "users_role"
    id = Column(Integer,primary_key=True,nullable=False,autoincrement=True)
    user = Column(String(60),nullable=False)
    user_id = Column(Integer,ForeignKey("users.id"))
    permission = Column(Integer,ForeignKey("rule.id"))
    user_permission = relationship("UserModel",back_populates="permissions",lazy="joined")
    rule = relationship("RuleModel",back_populates="user_permission",lazy="joined")

