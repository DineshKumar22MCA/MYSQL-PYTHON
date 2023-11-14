from  tabulate import tabulate
import mysql.connector

con=mysql.connector.connect(host="localhost",user="root",password="iamgroot@#$11",database="logic")

cur=con.cursor()
sql="select * from employees"
cur.execute(sql)
result=cur.fetchall()
print(tabulate(result,headers=["id","ename","jobdesc","salary","branchID"]))

