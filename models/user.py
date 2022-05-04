from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

from models import AbstractModel


class User(AbstractModel):
    __tablename__ = 'users'
    pk = Column(Integer, primary_key=True)
    phone_number = Column(String(50), nullable=False)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=True)
    email = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)
    date_of_birth = Column(String(50), nullable=False)
    address = Column(String(50), nullable=False)
    payment_methods = relationship("PaymentMethod", back_populates="user")

    def __init__(self, phone_number, first_name, last_name, email, password, date_of_birth, address, *args, **kwargs):
        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.date_of_birth = date_of_birth
        self.address = address

    def json(self):
        return {
            'phone_number': self.phone_number,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'password': self.password,
            'date_of_birth': self.date_of_birth,
            'address': self.address,
        }
