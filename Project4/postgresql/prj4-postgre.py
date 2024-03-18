#importing lib
import psycopg2

#connect to DB
connector = psycopg2.connect(database="prj4", user="postgres", password= "Hesam1993", host="localhost", port=5432)

#cursor
cursor = connector.cursor()

#Calling data from oracle
cursor.execute('SELECT * from test')
result = cursor.fetchall()

#printing the result
for row in result:
    print (row)
    
#closing
cursor.close()
connector.close()