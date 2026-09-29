import mysql.connector

# #establish connection between mysql and python code
# con=mysql.connector.connect(user="root",password="aleena",host="localhost")
# # return the connection object
# print(con)
#
# #cursor object --for executing sql queries
# c=con.cursor()
#
# query="create database school_db"
# c.execute(query)
# print("database file created")
# c.close()
# con.close()


#creating table
con=mysql.connector.connect(user="root",password="aleena",host="localhost",database="school_db")

c=con.cursor()
query="""create table student(roll_no int not null primary key,
       name varchar(20),
       age int, 
       place varchar(20),
       phone varchar(10),
       total_marks int)"""

c.execute(query)
print("table created")