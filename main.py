import random
import re
import sys
from abc import abstractmethod
import os

from sqlalchemy import create_engine, Column, Integer, ForeignKey, DateTime, String, MetaData, TIMESTAMP, func, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('postgresql+psycopg2://postgres:12345@127.0.0.1:5432/lab2db')
metadata = MetaData()
Session = sessionmaker(bind=engine)

Base = declarative_base()

Base.metadata.create_all(engine)

session = Session()


def write_from_csv_to_database(csv_filename, sections_to_search):
    with open(os.path.join(os.path.dirname(__file__), csv_filename), 'r+') as file:
        for part in re.split(r'\n\n+', file.read()):
            rows = part.split('\n')
            for row in rows:
                for section_name in sections_to_search:
                    if section_name == row.strip():
                        cls = getattr(sys.modules[__name__], section_name)
                        for row in rows[1:]:
                            args = row.split(',')
                            try:
                                obj = cls(*args)
                                if section_name == 'PaymentMethod':
                                    user = User.get_by_id(random.randint(1, len(rows) - 1))
                                    user.payment_methods.append(obj)
                                    user.save()
                                obj.save()
                            except:
                                raise AttributeError('You are doing something wrong buddy')


Base = declarative_base()

Base.metadata.create_all(engine)


class AbstactModel(Base):
    __abstract__ = True

    def save(self):
        session.add(self)
        session.commit()

    @classmethod
    def get_by_id(cls, pk):
        return session.query(cls).filter_by(pk=pk).first()


class User(AbstactModel):
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

    def __init__(self, phone_number, first_name, last_name, email, password, date_of_birth, address):
        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.date_of_birth = date_of_birth
        self.address = address


class PaymentMethod(AbstactModel):
    __tablename__ = 'paymentMethods'
    pk = Column(Integer, primary_key=True)
    payment_system = Column(String(50), nullable=True)
    card_number = Column(String(50), nullable=True)
    expire_date = Column(String(50), nullable=True)
    cvv = Column(String(8), nullable=True)
    country = Column(String(50), nullable=True)
    user_pk = Column(Integer, ForeignKey('users.pk'), nullable=False)
    user = relationship("User", back_populates="payment_methods")

    def __init__(self, payment_system, card_number, expire_date, cvv, country):
        self.payment_system = payment_system
        self.card_number = card_number
        self.expire_date = expire_date
        self.cvv = cvv
        self.country = country


Base.metadata.create_all(engine)

if __name__ == '__main__':
    write_from_csv_to_database('data.csv', ['User', 'PaymentMethod'])
