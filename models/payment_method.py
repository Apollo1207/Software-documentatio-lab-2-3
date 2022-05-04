from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship,backref

from models import AbstractModel


class PaymentMethod(AbstractModel):
    __tablename__ = 'paymentMethods'
    pk = Column(Integer, primary_key=True)
    payment_system = Column(String(50), nullable=True)
    card_number = Column(String(50), nullable=True)
    expire_date = Column(String(50), nullable=True)
    cvv = Column(String(8), nullable=True)
    country = Column(String(50), nullable=True)
    user_pk = Column(Integer, ForeignKey('users.pk'), nullable=False)
    user = relationship("User", back_populates="payment_methods")

    def __init__(self, payment_system, card_number, expire_date, cvv, country, *args, **kwargs):
        self.payment_system = payment_system
        self.card_number = card_number
        self.expire_date = expire_date
        self.cvv = cvv
        self.country = country

    def json(self):
        return {
            'payment_system': self.payment_system,
            'card_number': self.card_number,
            'expire_date': self.expire_date,
            'cvv': self.cvv,
            'country': self.country,
        }
