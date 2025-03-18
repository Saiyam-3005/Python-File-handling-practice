import csv
f=["name","cost","quantity",]
filename="items.csv"
h=str(input("do you want to update the items.csv file Y/N:"))
if h=="Y":
    n=int(input("enter the number of rows to be added:"))
    i2=[]
    for i in range(0,n):
        i=str(input("enter the name of the object:"))
        c=int(input("enter the cost of the itme:"))
        q=int(input("enter the quantity of the item:"))
        p=[i,c,q]
        i2.append(p)
    with open(filename,'w',newline='') as g:
        w=csv.writer(g,delimiter=',')
        w.writerow(f)
        w.writerows(i2)
        print("done")
    g.close()
y=str(input("do you want to search any item Y/N:"))
if y=="Y":
    f=open(filename,"r")
    r=csv.reader(f)
    name=str(input("enter the name of the item to be searched:"))
    for row in r:
        if row[0]==name:
            print(row)

    
