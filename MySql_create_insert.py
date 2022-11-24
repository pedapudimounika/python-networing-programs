import pymysql.cursors
import pdb

dataBase = pymysql.connect(host= 'localhost',
                        user = 'root',
                        password = 'admin',
                        database = 'demo2',
                        cursorclass = pymysql.cursors.DictCursor)

# preparing a cursor object
cursorObject = dataBase.cursor()
  
# creating table
studentRecord = """CREATE TABLE STUDENT (NAME  VARCHAR(20) NOT NULL, BRANCH VARCHAR(50), ROLL INT NOT NULL, SECTION VARCHAR(5), AGE INT )"""
				   
				   
cursorObject = dataBase.cursor()
#insert  into the table
 
sl = "INSERT INTO STUDENT (NAME, BRANCH, ROLL, SECTION, AGE)\
VALUES (%s, %s, %s, %s, %s)"
val = [("Nikhil", "CSE", "98", "A", "18"),
       ("Nisha", "CSE", "99", "A", "18"),
       ("Rohan", "MAE", "43", "B", "20"),
       ("Amit", "ECE", "24", "A", "21"),
       ("Anil", "MAE", "45", "B", "20"),
       ("Megha", "ECE", "55", "A", "22"),
       ("Sita", "CSE", "95", "A", "19")]


#query = "SELECT * FROM STUDENT where AGE >=20"	   
#breakpoint()
try:
	cursorObject.executemany(studentRecord, sl, val)
	dataBase.commit()
	myresult = cursorObject.fetchall()
   

except:
	dataBase.rollback()

	# for x in myresult:
     # print(x)

# disconnecting from server
dataBase.close()
  

						
						
						
						
						
						# with db.cursor() as cursor:

		# sql = "SELECT *FROM student "
		# cursor.execute(sql)
		# result = cursor.fetchall()
		# print(result)

