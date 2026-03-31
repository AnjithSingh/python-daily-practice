
'''

import sqlite3

conn = sqlite3.connect('customer.db')

#create a cursor
c = conn.cursor()


#Create a table
c.execute("""CREATE TABLE customers (
      first_name text,
      last_name text,
      email text
         )""")

# SQLITE has 5 DATATYPES 
# NULL
# INTEGER
# REAL
# TEXT
# BLOB


# Commit our command 
conn.commit()

# CLose our connection 

conn.close()

'''






'''
import sqlite3

conn = sqlite3.connect('customer.db')

#create a cursor
c = conn.cursor()


c.execute("insert into customers values('ALia' , 'bhatt' , 'aliabhatt@gmail.com')")

print("command executed successfully")

# Commit our command 
conn.commit()

# CLose our connection 

conn.close()

'''

import sqlite3

conn = sqlite3.connect('customer.db')

#create a cursor
c = conn.cursor()

many_customers = [('punnet' , 'superstar' , 'punnet#superstar.com'),
                  ('kiara','advani' , 'kiara@advani.com'),
                  ('duran' , 'dhar' , 'dhuran@dhar.com')]

c.executemany("insert into customers values(?,?,?)",many_customers)

print("command executed successfullyyy")

# Commit our command 
conn.commit()

# CLose our connection 

conn.close()
