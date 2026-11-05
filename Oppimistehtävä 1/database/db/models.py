from sqlalchemy import Column, Integer, String, JSON
from sqlalchemy.orm import declarative_base

Base = declarative_base()

# Example: table for JSONPlaceholder "users"
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    website = Column(String)
    address = Column(JSON)
    company = Column(JSON)

class DataProtectedUser(Base):
    __tablename__ = "dataprotectedusers"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    website = Column(String)
    address = Column(JSON)
    company = Column(JSON)