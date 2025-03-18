def display(name):
    t=open(name)
    u=t.readline()
    c=0
    while u:
       g= u.split()
       for i in g:
            if i[0]=="t" or i[0]=="T":
                c=c+1
       u=t.readline()
    t.close()
name=str(input("enter the name of the file in the.txt format:"))
print(display(name))
