# lib/models.py
from sqlalchemy import ForeignKey, Column, Integer, String
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    founding_year = Column(Integer())
    freebies = relationship('Freebie', back_populates='company')

    def __repr__(self):
        return f'<Company {self.name}>'

class Dev(Base):
    __tablename__ = 'devs'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    freebies = relationship('Freebie', back_populates='dev')
    given_freebies = relationship('Freebie', back_populates='giver', foreign_keys='Freebie.giver_id')

    def __repr__(self):
        return f'<Dev {self.name}>'

class Freebie(Base):
    __tablename__ = 'freebies'

    id = Column(Integer(), primary_key=True)
    item_name = Column(String())
    value = Column(Integer())
    dev_id = Column(Integer(), ForeignKey('devs.id'))
    company_id = Column(Integer(), ForeignKey('companies.id'))
    dev = relationship('Dev', back_populates='freebies')
    company = relationship('Company', back_populates='freebies')
    giver_id = Column(Integer(), ForeignKey('devs.id'))
    giver = relationship('Dev', back_populates='given_freebies', foreign_keys=[giver_id])

    def __repr__(self):
        return f'<Freebie {self.item_name}>'
