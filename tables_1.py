import mysql.connector

db=mysql.connector.connect(host= 'localhost',
                        user = 'root',
                        password = 'admin',
                        database = 'demo2',)
cursor=db.cursor()

query="SELECT * FROM MyTable"
cursor.execute(query)
for row in cursor:
   print(row)