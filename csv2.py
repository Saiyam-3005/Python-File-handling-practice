'''Name, Age, Qualification, Experience Ananya,32,PG,8
Then, write a menu driven program to perform the following operations on the
file:
(i) Append record(s) to the file
(ii) Display all the data from the file
(iii) Display all the records with Age<30
(iv) Delete a record with given name and age (to be input from the user).'''

import csv
f=["name","age","qualification","experinence"]
r=["Ananya","32","PG","8"]
with open("data.csv","w",newline='')as g:
    w=csv.writer(g,delimiter=',')
    w.writerow(f)
    w.writerow(r)
g.close()
def append():
    n=int(input("enter the number of rows to be added:"))
    i2=[]
    for i in range(0,n):
        i=str(input("enter the name:"))
        c=int(input("enter the age:"))
        q=str(input("enter the quanlification:"))
        l=int(input("enter the experinence:"))
        p=[i,c,q,l]
        i2.append(p)
    with open("data.csv",'a',newline='') as g:
        w=csv.writer(g,delimiter=',')
        w.writerows(i2)
        print("done")
    g.close()
def read():
    f=open("data.csv","r")
    r=csv.reader(f)
    for i in r:
        print(i)
    f.close()
def delete():
        l= list()
        m=input("Please enter the name to be deleted.")
        with open('data.csv', 'r') as r:
            read = csv.reader(r)
            for row in read:
                l.append(row)
                for f in row:
                    if f == m:
                        l.remove(row)
        with open('data.csv', 'w') as w:
            wr= csv.writer(w)
            wr.writerows(l)
            w.close()
def reads():
    f=open("data.csv","r")
    r=csv.reader(f)
    for i in r:
        if i[1]<"30":
            print(i)
print('MAIN MENU')
print('1.append the file')
print("2.Read all data from a file ")
print("3.Display all the records with Age<30")
print("4..elete a record with given name")
k=1
while k==1:
    h=int(input("ENTER THE SERIAL NUMBER OF THE PROGRAMME TO BE RUN:"))
    if h==1:
        append()
    if h==2:
         read()
    if h==3:
         reads()
    if h==4:
       delete()




    
