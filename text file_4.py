def create():
    g=open("story.txt","w+")
    n=int(input("enter the number of lines to be printed:"))
    for i in range(0,n):
        f=str(input("enter the""line of the document:"))
        g.write(f)
        g.write("\n")
    g.close()
def upper():
    r=open("story.txt","r")
    count=0
    u=r.read(1)
    while u:
        u=r.read(1)
        if u.isupper():
            count=count+1
    return count
    r.close()
create()
print("total number of uppercase letters are:",upper())
print("by saiuam jain")

