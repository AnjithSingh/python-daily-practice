
# Perform CRUD operations

from sqlalchemy.orm import sessionmaker

from models import User , engine 

Session = sessionmaker(bind = engine ) # bind tells where we are making these transactions or in which db we are connecting

session = Session()

'''
user = User(name = "Anjith Singh" , age = 20)
user2 = User(name = "jaan" , age = 20)
user3 = User(name = "kaam" , age = 21)

session.add(user)
session.add_all([user2,user3])

session.commit

'''

# users = session.query(User).all()


# users = session.query(User).filter_by(id = 1).all() #first # one_or_none

user.name = "a diffrent name" # the name will change
# print(users[0]) 
