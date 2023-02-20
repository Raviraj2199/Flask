import time
import csv
import sys
import sqlite3


def waittime5():
  for i in range(3,0,-1):
    print(i)
    time.sleep(2)



def waittime3():
  for i in range(3,0,-1):
    print(i)
    time.sleep(1)


try:
     print("opening csv file to read")
     waittime3()
     with open("student_info.csv",'r')as fin:
        dr = csv.DictReader(fin)
        student_info = [(i['id'],i['name'],i['age'],i['phone'])for i in dr]
        print("loading csv file that is read")
        waittime3()
        print(student_info)

        #connect to sqlite
     sqliteConnection = sqlite3.connect('mydb1.db')
     cursor = sqliteConnection.cursor()
     print("successfully connected to db")


     #create student table
     cursor.execute('create table if not exist student_info(id int ,name varchar(20),age int ,phone int);')
     print("sucessfully student_info table created")
     waittime3()

     #insert data into table
     cursor.executemany("insert into student_info(id,name,age,phone)values(?,?,?,?)",student_info)
     print('successfully inserted data into students tables')

     #show student table
     cursor.execute("select * from student_info")
     print("retrieving data")

     #view the results
     result = cursor.fetchall()
     print("preparing the display the data")
     waittime3()
     print(result)
     
     #commit work and close connection
     sqliteConnection.commit()
     cursor.close()

    


except sqlite3.Error as error :
    print("\nError while connecting to sqlite",error)

finally:
    if (sqliteConnection):
        sqliteConnection.close()
        print("\n sqlite connection is closed")