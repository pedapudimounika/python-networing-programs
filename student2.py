import pymysql.cursors

db = pymysql.connect(host= 'localhost',
                        user = 'root',
                        password = 'admin',
                        database = 'demo1',
                        cursorclass = pymysql.cursors.DictCursor)

with db.cursor() as cursor:
		sql = "SELECT *FROM student "
		cursor.execute(sql)
		result = cursor.fetchall()
		print(result)

