from sqlalchemy import Column, Integer, String
from boilerplate.database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    firstName = Column(String)
    lastName = Column(String)
    email = Column(String)
    password = Column(String)
