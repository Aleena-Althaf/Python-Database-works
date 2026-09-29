import mysql.connector
con=mysql.connector.connect(user="root",password="aleena",host="localhost",database="school_db")
# print(con)




print(con)
c=con.cursor()

query="select * from student where roll_no=%s" #read a specific record
data=(101,)
c.execute(query,data)
record=c.fetchone()

if record:
    print(record)
else:
    print("no record found")

c.close()