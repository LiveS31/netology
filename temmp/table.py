import sqlalchemy as sq
from sqlalchemy.orm import declarative_base
Base = declarative_base()

class Ya(Base):
    __tablename__ = "ya"
    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String)

class Vor(Base):
    __tablename__ = 'vor'
    id = sq.Column(sq.Integer, primary_key=True)
class Bor(Base):
    __tablename__ = 'Bor'
    id = sq.Column(sq.String, primary_key=True)

def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

