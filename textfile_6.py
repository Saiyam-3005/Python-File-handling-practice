print("FIRST CREATE A FILE :")
s=open("PRACTICLE4.txt","w")
n=int(input("enter the number of lines to be printed:"))
for i in range(0,n):
    t=str(input("enter:"))
    s.write(t)
    s.write("\n")
s.close()
def display():
    t=open("PRACTICLE4.txt","r")
    u=t.readline()
    while u:
        if u[-1]=="?"or u[-1]==".":
            return u
        u=t.readline()
    t.close()
print(display())
