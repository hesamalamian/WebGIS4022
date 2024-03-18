#importing lib
import cx_Oracle

#connect to DB
connector = cx_Oracle.connect('System/Hesam1993@localhost:1521/orcldata')

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