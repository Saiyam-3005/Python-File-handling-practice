#employee record
import pickle
import os
def insert():
    f=open("employeedata.dat","ab")
    n=int(input("enter the number for employee for whom data is to be added:"))
    for i in range(0,n):
        empno=str(input("enter the employee number:"))
        empname=str(input("enter the name:"))
        salary=int(input("enter the salary:"))
        department=str(input("enter the department name:"))
        rec={"EMPLOYEE NUMBER":empno,"NAME":empname,"SALARY":salary,"DEPARTMENT":department}
        pickle.dump(rec,f)
def read():
    f=open("employeedata.dat","rb")
    while True:
        try:
            rec=pickle.load(f)
            print("EMPLOYEE NUMBER\tEMPLOYEE NAME\tSALARY\tDEPARTMENT")
            print(rec["EMPLOYEE NUMBER"],"\t\t",rec["NAME"],"\t\t",rec["SALARY"],"\t\t",rec["DEPARTMENT"])
        except EOFError:
            break
    f.close()
def search():
    f=open("employeedata.dat","rb")
    flag=0
    r=str(input("enter employee name to be searched:"))
    while True:
        try:
            s=pickle.load(f)
            if s['NAME']==r:
                print(s)
                flag=1
                break
        except  EOFError:
            pass
    if flag==0:
        print("record not found")
    f.close()
print("MAIN MENU")
print("1.read the data in tabular form")
print("2.search from data on basis of empployee number:")
print("3.insert data")
print("PRESS 0 TO EXIT THE CODE")
while True:
    c=int(input("enter the serial number of the programme"))
    if c==0:
        print("THANK YOU")
        break
    if c==1:
        read()
    if c==2:
        search()
    if c==3:
        insert()
    
    



























             
