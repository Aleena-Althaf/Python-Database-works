# define a class to perform database operations on vehicle table
# create class named vehicleListCreateRetrieveUpdateDelete
# with methods
#     list()
#     create()
#     retrieve()
#     update()
#     delete()
# table:id,brand,model,type,price,year

import mysql.connector
class VehicleListCreateRetrieveUpdateDelete:
    def __init__(self):
        self.con=mysql.connector.connect(user='root',password='Anagha',host='localhost',database='Vehicle_db')

        self.c=self.con.cursor()
        print("successfully connected")

    def list(self):
        #Reading all records from db file
        query ='select * from vehicle'
        self.c.execute(query)
        record =self.c.fetchall()
        if record:
            for row in record:
                print(row)
        else:
            print('no record found')


    def create(self,brand,model,type,price,year):
            #creating a new records
            query ='insert into vehicle(brand,model,type,price,year) values(%s,%s,%s,%s,%s)'
            data = (brand,model,type,price,year)
            self.c.execute(query, data)
            self.con.commit()



    def retrieve(self,id):

        query="select * from vehicle where id=%s"
        data=(id,)
        self.c.execute(query,data)
        record=self.c.fetchone()

        if record:
            print(record)
        else:
            print("No Record Found")


    def delete(self,id):
        query='delete from vehicle where id=%s'
        data=(id,)
        self.c.execute(query,data)
        self.con.commit()
        if self.c.rowcount > 0:
            print("Data is deleted")
        else:
            print("No Record Found")



    def update(self,id,brand,model,type,price,year):
        query='update vehicle set id=%s,brand=%s,model=%s,type=%s,price=%s,year=%s'
        data=(id,brand,model,type,price,year)
        self.c.execute(query,data)
        self.con.commit()
        if self.c.rowcount > 0:
            print("updated successfully")
        else:
            print("No Record Found")


v=VehicleListCreateRetrieveUpdateDelete()
# v.list()
# v.create("Toyota","Innova",'car',2500000,2024)
# v.retrieve(1)
# v.delete(2)
# v.update(4,"BMW", "X5", 'car', 7000000, 2025)