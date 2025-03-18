import mysql.connector
data=mysql.connector.connect(host="localhost",user="root",passwd="jain12345",charset='utf8')
mycursor=data.cursor()
mycursor.execute("CREATE DATABASE XII")
print("DATABASE CREATED")
mycursor.execute("use XII")
def CREATE_TABLE():
    print("..........CREATING TABLE.................")
    qr="create table public(pno int(2), pname char(10) , pqty float(3,2))"
    mycursor.execute(qr)
    print("table created")
    mycursor.execute("show tables")
    print(mycursor)
    r=mycursor.fetchall()
    print(type(r))
    print(r)
    print("tables are:")
    for i in r:
        print(i)

def describe_table():
    print("...........DESCRIBING TABLE...........")
    qry="DESCRIBE public"
    mycursor.execute(qry)
    row = mycursor.fetchall()
    for x in row:
        print(x)

def insert_values():
    print("..........INSERTING RECORDS.....")
    while True:
        pno= int(input("enter pno: "))
        pname= input("enter pname: ")
        pqty=float(input("enter quantity: "))
        qry="insert into public values("+str(pno)+",'"+pname+"',"+str(pqty)+")"
        mycursor.execute(qry)
        print("row adaded")
        ch=input("do you want to enter more y/n: ")
        if ch=="n":
            break
    data.commit()
    mycursor.execute("select * from public")
    rec=mycursor.fetchall()
    print(rec)

def update_values():
    ans='y'
    while True:
        print("............UPDATING RECORDS.....")
        productno=int(input("Enter pno for which record is to be updated: "))
        newqty=float(input("Enter new quantity: "))
        qry="Update public set pqty={} where pno='{}' ".format (newqty,productno)
        mycursor.execute(qry)
        data.commit()
        print("row updated")
        ch= input("do you want to enter more y/n: ")
        if ch=="n" or ch=="N":
            break
    mycursor.execute("select pno,pname,pqty from public")
    rec=mycursor.fetchall()
    for row in rec:
        print(row)

def delete_value():
    ans='y'
    while True:
        print("...............DELETING RECORDS.......")
        productno=int(input("Enter pno for which record is to be deleted: "))
        Qry="DELETE FROM public where pno= '{}'".format(productno)
        mycursor.execute(Qry)
        data.commit()
        print("row deleted")
        ch= input("do you want to enter more y/n: ")
        if ch=="n" or ch=="N":
            break
    mycursor.execute("select pno,pname,pqty from public")
    rec=mycursor.fetchall()
    for row in rec:
        print(row)

print("*"*40)
print("********WELCOME TO MENU DRIVEN PROGRAM OF MYSQL CONNECTIVITY***********")
print("FUNCTIONS AVAILABLE")
print("1.CREATE TABLE")
print("2. DESCRIBE TABLE")
print("3.INSERT VALUES")
print("4.UPDATE VALUES")
print("5. DELETE RECORDS")
print("6. EXIT")

while True:
    ch=int(input("Enter your choice: "))
    if ch==1:
        CREATE_TABLE()
    elif ch==2:
        describe_table()
    elif ch==3:
        insert_values()
    elif ch==4:
        update_values()
    elif ch==5:
        delete_value()
    else:
        print("THANK YOU FOR VISTING")
        print("PROGRAMME ENDED")
        break
        
            




