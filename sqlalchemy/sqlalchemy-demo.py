from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String
from sqlalchemy import MetaData
import sqlalchemy
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import insert, select

Base = declarative_base()
engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)


class User(Base):
    __tablename__ = 'user_account'

    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    fullname = Column(String)

    def __repr__(self):
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"


with engine.connect() as conn:
    conn.execute(insert(User.__table__).values(
        name='spongebob', fullname="Spongebob Squarepants"))

    for row in conn.execute(select(User.__table__)):
        print(row)
