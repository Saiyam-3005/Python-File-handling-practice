s=open("PRACTICLE3.txt","w")
n=int(input("enter the number of lines to be printed:"))
for i in range(0,n):
    t=str(input("enter:"))
    s.write(t)
    s.write("\n")
s.close()
def display():
    t=open("PRACTICLE3.txt","r")
    x=str(input("enter the starting letter:"))
    c=0
    l=t.readline()
    while l:
        if l[0]==x:
            print(l)
            c+=1
        l=t.readline()
    print("total number of line starting with this letter is:",c)
    t.close()
    
def reverse():
    t=open("PRACTICLE3.txt","r")
    u=t.readlines()
    for i in u[::-1]:
        print(i)
print("MAIN MENU")
print("1.display and count line starting with any letter:")
print("2.read a line in reverse order")
print("NOTE PRESS 0 TO EXIT")
while True:
    z=int(input("enter the serial number of the programme to be performed:"))
    if z==0:
        print("THABK YOU")
        break
    if z==1:
        display()
    if z==2:
        reverse()



