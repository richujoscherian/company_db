from mysql import connector
import datetime
class db_connect:
    def get_connected(self):
        try:
            self.connection=connector.connect(
                host="localhost",
                user="root",
                password="Richu@2003",
                database="company_db"
        
            )
            return self.connection
        except Exception as e:
            return None
class employee_manager(db_connect):
        def get(self):
            try:

                self.connect=super().get_connected()
                self.cursor=self.connect.cursor()

                query="select * from employee"

                self.cursor.execute(query)
                record=self.cursor.fetchall()
                for data in record:
                    print(record)
                return record
            except Exception as e:
                return e
        def post(self,**kwargs):
            try:
                self.connect=super().get_connected()
                self.cursor=self.connect.cursor()

                query=""" insert into employee(name,place,mobile,email,department,salary,joining_date) values(%s,%s,%s,%s,%s,%s,%s)"""
                values=[v for v in kwargs.values()]

                self.cursor.execute(query,values)
                print("successfully added")
                self.connect.commit()
            except Exception as e:
                return e
        def get_object(self,id):
            try:
                self.connect=super().get_connected()
                self.cursor=self.connect.cursor()
                query="select * from employee where id=%s "
                value=(id,)
                self.cursor.execute(query,value)
                record=self.cursor.fetchone()
                return record
            except Exception as e:
                return e

        def put(self,id,**kwargs):
            try:
                self.connect=super().get_connected()
                self.cursor=self.connect.cursor()
                record=self.get_object(id=id)
                if record!= None:
                    placeholder=""
                    for k in kwargs.keys():

                        placeholder+=k + "=%s,"
                    placeholder=placeholder.rstrip(",")

                    query=f"update employee set {placeholder} where id=%s"
                    values=[k for k in kwargs.values()]
                    values.append(id)

                    self.cursor.execute(query,values)
                    self.connect.commit()
                    print("employee updated succesfully")
                else:
                    print("employee not found")
            except Exception as e:
                return e


        def delete(self,id):
                try:
                    self.connect=super().get_connected()
                    self.cursor=self.connect.cursor()

                    record=self.get_object(id=id)
                    if record!= None:
                        query="delete from employee where id=%s"
                        value=(id,)
                        self.cursor.execute(query,value)
                        self.connect.commit()
                    print("employee deleted succesfully")
                except Exception as e:
                    return e

        def retrieve(self,id):
            try:
                self.connect=super().get_connected()
                self.cursor=self.connect.cursor()

                query="select * from employee where id=%s"
                value=(id,)
                self.cursor.execute(query,value)
                record=self.cursor.fetchone()
                print(record)
            except Exception as e:
                return e


obj1=employee_manager()
# obj1.post(name="Richu",place="kottayam",mobile="62380238479",email="richu@gmail.com",department="CSE",salary="50000",joining_date=datetime.date.today())
obj1.put(1,name="achu")
obj1.get()



