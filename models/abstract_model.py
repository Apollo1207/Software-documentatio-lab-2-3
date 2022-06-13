from abc import abstractmethod

from database import Base, Session, session


class AbstractModel(Base):
    __abstract__ = True

    @classmethod
    def __commit(cls):
        try:
            session.commit()
        except Exception as e:
            raise e

    def save(self):
        session.add(self)
        self.__commit()

    @classmethod
    def get_by_pk(cls, pk):
        return session.query(cls).filter_by(pk=pk).first()

    @classmethod
    def get_all(cls):
        return session.query(cls).all()

    def delete(self):
        session.delete(self)
        self.__commit()

    @abstractmethod
    def json(self):
        raise NotImplementedError
