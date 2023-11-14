from tabulate import tabulate
import mysql.connector

con=mysql.connector.connect(host="localhost",user="root",password="iamgroot@#$11",database="python_db")

def insert(name,age,city):
    cur=con.cursor()
    sql="insert into users(uname,age,city) values (%s,%s,%s)"
    user=(name,age,city)
    cur.execute(sql,user)
    con.commit()
    print("data insert successfully")

def update(name,age,city,id):
    cur=con.cursor()
    sql="update users set uname=%s,age=%s,city=%s where id=%s"
    user=(name,age,city,id)
    cur.execute(sql,user)
    con.commit()
    print("updated successfully")
def select():
    cur=con.cursor()
    sql="select * from users"
    cur.execute(sql)
    res=cur.fetchall()
    print(tabulate(res,headers=["id","uname","age","city"]))

def delete(id):
    cur=con.cursor()
    sql="delete from users where id=%s"
    user=(id,)
    cur.execute(sql,user)
    con.commit()
    print("deleted successfully")



while True:
    print("1.insert")
    print("2.update")
    print("3.select")
    print("4.delete")
    print("5.exit")
    choise =int(input("enter the option : "))
    if choise == 1:
        name=input("enter the name : ")
        age=int(input("enter the age : "))
        city=input("enter the city : ")
        insert(name,age,city)
    elif choise ==2:
        id = int(input("enter the id : "))
        name=input("enter the name : ")
        age= int(input("enter the age :"))
        city=input("enter the city : ")
        update(name,age,city,id)
    elif choise==3:
        select()
    elif choise ==4:
        id=input("enter the id : ")
        delete(id)
    elif choise==5:
        quit()
    else:
        print("invalide selection, please try again ")


