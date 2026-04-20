import sys
import os
import psycopg2

file = open('name.txt' , 'r')

x = file.read()
try:
    connection = psycopg2.connect(
        database = sys.argv[1],
        user = os.environ.get('PGUSER'),
        password = os.environ.get('PGPASSWORD'),
        host = os.envron.get('PGHOST'),
        port = os.environ.get('PGPORT'))
    cursor = connection.cursor()
    query = "select jersey_no from players where name = '{}'".format(x)
    cursor.execute(query)
    result = cursor.fetchall()
    for i in result:
        print(i[0])
    cursor.close()
except(Exception,psycopg2.DatabaseError) as error:
    print(error)
finally:
    connection.close()



