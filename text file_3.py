#number of times a word occurs
s=open("PRACTICLE2.txt","w")
n=int(input("enter the number of lines to be printed:"))
for i in range(0,n):
    t=str(input("enter:"))
    s.write(t)
    s.write("\n")
s.close()
def count():
    t=open("PRACTICLE2.txt","r")
    d=str(input("enter the word to be find:"))
    c=0
    x=t.read()
    w=x.split()
    for i in w :
        if i==d:
            c+=1
    r=print("my occurs:",c,"times")
    return r
    t.close()
print(count())
