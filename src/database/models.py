from sqlalchemy import Column, Integer, String, Date
from src.database.db import Base

class Contact(Base):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone_number = Column(String, unique=True, nullable=False)
    birth_date = Column(Date, nullable=False)
    additional_info = Column(String, nullable=True)
