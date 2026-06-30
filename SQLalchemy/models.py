''' from sqlalchemy import create_engine , Column , Integer , String , ForeignKey , Table
from sqlalchemy.orm import relationship , declarative_base , sessionmaker

DATABASE_URL = "sqlite://college.db"

engine = create_engine(DATABASE_URL,echo = False)
'''


from sqlalchemy import create_engine , Column , Integer , String

from sqlalchemy.orm import declarative_base

db_url = "sqlite:///databasehai.db"

engine = create_engine(db_url)

base = declarative_base()


class User(base):
    __tablename__ = "Users"

    id = Column(Integer , primary_key = True)
    name = Column(String)
    age = Column(Integer)







base.metadata.create_all(engine)   # it will create the database and all the tables we needed

