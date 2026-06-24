
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
'''






'''

import sqlite3

conn = sqlite3.connect('customer.db')

c = conn.cursor()

c.execute("select * from customers")
#fetchone
#fetchmany(3)
#fetchall

#print(c.fetchall()[0])
print(c.fetchall())


conn.commit()
conn.close()

'''

'''

import sqlite3

conn = sqlite3.connect('customer.db')

c = conn.cursor()

c.execute("select * from customers")

items = c.fetchall()

for item in items:
    print(item)



conn.commit()
conn.close()

'''


'''
import sqlite3

conn = sqlite3.connect('customer.db')

c = conn.cursor()

c.execute("select * from customers")

items = c.fetchall()

for item in items:
    print(item[0])



conn.commit()
conn.close()

'''

'''

import sqlite3

conn = sqlite3.connect('customer.db')

c = conn.cursor()

c.execute("select * from customers")

items = c.fetchall()

for item in items:
    print(item[0] + " " + item[1])



conn.commit()
conn.close()

'''

