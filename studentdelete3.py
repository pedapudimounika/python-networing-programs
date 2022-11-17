import pymysql

db = pymysql.connect(host= 'localhost',
                        user = 'root',
                        password = 'admin',
                        database = 'demo1',
                        cursorclass = pymysql.cursors.DictCursor)

cursor = db.cursor()
query = 'delete from student where age>23'

try:
			cursor.execute(query)
			db.commit()
except:
			db.rollback()
db.close()