import mysql.connector
class BookListCreateRetrieveUpdateDelete:
    def __init__(self):
        self.connection=mysql.connector.connect(user="root",password="aleena",host="localhost",database="library_db")
        print(self.connection)
        self.cursor=self.connection.cursor()
        print("successfully connected")


    def list(self):
        #reading all records from db table
        query="select * from book"
        self.cursor.execute(query)
        records=self.cursor.fetchall()
        if records:
            for row in records:
                print(row)
        else:
            print("No records found")

    def create(self,title,author,price,pages,language):
        #creating a new record
        query="insert into book values(%s,%s,%s,%s,%s)";
        data=(title,author,price,pages,language)
        self.cursor.execute(query,data)
        self.connection.commit()
        print("inserted daa successfully")


    def retrieve(self,id):
        query="select * from book where id=%s"
        data=(id,)
        self.cursor.execute(query,data)
        record=self.cursor.fetchone()
        if record:
            print(record)
        else:
            print("no record found")

    def update(self,id,title,author,price,pages,language):
        query="update book set title =%s,author=%s,price=%s,pages=%s,language=%s where id=%s"
        data=(title,author,price,pages,language)
        self.cursor.execute(query,data)
        self.connection.commit()
        if self.cursor.rowcount > 0:
            print("updated data successfully")
        else:
            print("no record found")



    def delete(self,id):
        query="delete from book where id=%s"
        data=(id,)
        self.cursor.execute(query,data)
        self.connection.commit()
        if self.cursor.rowcount>0:
            print ("deleted data succesfully")
        else:
            print("no record found")

b=BookListCreateRetrieveUpdateDelete()
b.list()
b.create('ABC','john',300,500,'english')
b.retrieve(2)
b.delete(3)
b.update('ABC','john',300,500,'english')