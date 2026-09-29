import mysql.connector
con=mysql.connector.connect(user="root",password="aleena",host="localhost",database="school_db")
print(con)

c=con.cursor()
#insert into tablename values (............);
query="insert into student values(%s,%s,%s,%s,%s,%s)"
data=(101,"arun",20,"ekm","908765432",145)
c.execute(query,data)
con.commit()
print("data inserted successfully")
c.close()
con.close()