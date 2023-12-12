#!/usr/bin/env python3

# Script goes here!
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Company, Dev, Freebie

engine = create_engine('sqlite:///freebies.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Create sample data
company1 = Company(name="TechCorp", founding_year=2000)
company2 = Company(name="CodeHub", founding_year=2010)
dev1 = Dev(name="John Doe")
dev2 = Dev(name="Jane Doe")

freebie1 = Freebie(item_name="T-shirt", value=20, company=company1, dev=dev1)
freebie2 = Freebie(item_name="Sticker", value=5, company=company2, dev=dev1)
freebie3 = Freebie(item_name="Laptop", value=1000, company=company1, dev=dev2)

# Add to session
session.add_all([company1, company2, dev1, dev2, freebie1, freebie2, freebie3])
session.commit()
