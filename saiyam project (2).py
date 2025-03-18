import csv
import os
filename="student details.csv"
def create():
    title=["name","vp number","class","sction","date of birth","father name","mother name","parents number","student number","address","email id"]
    n=int(input("enter the number of students to be added:"))
    i2=[]
    for i in range(0,n):
        b=int(input("enter the vp number:"))
        c=int(input("enter class:"))
        d=str(input("enter section:"))
        a=str(input("enter the name of the student:"))
        e=str(input("enter date of birth:"))
        f=str(input("enter father name:"))
        m=str(input("enter mother name:"))
        g=int(input("enter parents number:"))
        h=str(input("enter students number:"))
        i=str(input("enter address:"))
        j=str(input("enter email id:"))
        p=[a,b,c,d,e,f,m,g,h,i,j]
        i2.append(p)
    with open("student details.csv",'w',newline='') as g:
        w=csv.writer(g,delimiter=',')
        w.writerow(title)
        w.writerows(i2)
        print("done")
    g.close()
def search():
        f=open("student details.csv","r",newline='\r\n')
        r=csv.reader(f)
        name=str(input("enter the name of the student to be searched:"))
        for row in r:
            if row[0]==name:
                print(row)
        f.close()
def read():
    f=open("student details.csv","r",newline='\r\n')
    r=csv.reader(f)
    for i in r:
        print(i)
    f.close()
def remove():
       y=open('student details.csv','r',newline='\r\n')
       t=open('temperory.csv','w',newline='\r\n')
       j=input('Enter student name you want to delete:')
       p=csv.reader(y)
       s1=csv.writer(t)
       for r in p:
           if r[0]==j:
                pass
                print("Record Deleted")
           else:
             s1.writerow(r)
       y.close()
       t.close()
       os.remove("student details.csv")
       os.rename("temperory.csv","student details.csv")


def modify():
       print("MODIFY DETAIL")
       y=open("student details.csv",'r',newline='\r\n')
       t=open('temperory.csv','w',newline='\r\n')
       p=input('Enter student name you want to modify:')
       s=csv.reader(y)
       s1=csv.writer(t)
       for r in s:
           if r[0]==p:
               b=int(input("enter the new vp number:"))
               c=int(input("enter new class:"))
               d=str(input("enter new section:"))
               a=str(input("enter the new name of the student:"))
               e=str(input("enter new date of birth:"))
               f=str(input("enter father name:"))
               m=str(input("enter mother name:"))
               g=int(input("enter new parents number:"))
               h=str(input("enter new students number:"))
               i=str(input("enter new address:"))
               j=str(input("enter new email id:"))
               z=[a,b,c,d,e,f,m,g,h,i,j]
               s1.writerow(z)
               print("Record Modified")
           else :
                s1.writerow(r)
       y.close()
       t.close()
       os.remove("student details.csv")
       os.rename("temperory.csv","student details.csv")
       
print('MAIN MENU')
print('1.create the file')
print("2.serach a name from the file ")
print("3.Display all the records from a file")
print("4. delete a record with given name")
print("5. modify details of the given name")
print("0 to exit")
while True:
    print("*"*40)
    h=int(input("ENTER THE SERIAL NUMBER OF THE PROGRAMME TO BE RUN:"))
    if h==1:
     create()
    if h==2:
        search()
    if h==3:
        read()
    if h==4:
        remove()
    if h==5:
        modify()
    if h==0:
        print("THANK YOU")
        break
    
    
    



    
