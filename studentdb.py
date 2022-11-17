import pymysql

db = pymysql.connect(host= 'localhost',
                        user = 'root',
                        password = 'admin',
                        database = 'demo1',
                        cursorclass = pymysql.cursors.DictCursor)

cursor = db.cursor()
query = 'INSERT INTO student VALUES("john", "dell", 45, "57786f67hb")'

try:
			cursor.execute(query)
			db.commit()
except:
			db.rollback()
db.close()