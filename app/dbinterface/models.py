from sqlalchemy import Boolean, Column, ForeignKey, String
from sqlalchemy.dialects.mysql import INTEGER

from dbinterface.core import Base


class Users(Base):
    __tablename__ = "users"

    id = Column(INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    api_key = Column(String(256), nullable=False, unique=True)


class Transactions(Base):
    __tablename__ = "transactions"

    id = Column(INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    user_id = Column(INTEGER(unsigned=True), ForeignKey("users.id"), nullable=False)
    amount = Column(INTEGER, nullable=False)
    description = Column(String(256), nullable=False)
