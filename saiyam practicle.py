s=open("STORY.txt","w")
n=int(input("enter the number of lines to be printed minimum 5:"))
if n>=5:
    for i in range(0,n):
        t=str(input("enter the line :"))
        s.write(t)
        s.write("\n")
    s.close()
else:
    print("invalid input")
print("MAIN MENU")
print("1.tp count the number of words in the text fil")
print("2.to count the number of lines in the text file:")
print("3.to count number of character in the text file:")
print("4.to couht number of words starting with a vowel:")
print("5.no. of words ending with  questiion  mark:")
print("6.tell the length of the file:")
print("7.display word with length 5:")
print("NOTE PRESS 0 TO EXIT THE CODE:")

def count():
    t=open("STORY.txt","r")
    c=0
    x=t.read()
    w=x.split()
    for i in w :
            c+=1
    r=print("total words are:",c,)
    return r
    t.close()

def countl():
    t=open("STORY.txt","r")
    c=0
    x=t.readlines()
    w=len(x)
    r=print("total lines are :",w)
    return r
    t.close()

def ch():
    t=open("STORY.txt","r")
    c=0
    x=t.read()
    w=x.split()
    for i in w :
        for r in i:
            c+=1
    r=print("total character  are:",c,)
    return r
    t.close()

def countv():
    t=open("STORY.txt","r")
    c=0
    x=t.read()
    w=x.split()
    for i in w :
        if i[0] in "aeiouAEIOU":
            c+=1
    r=print("total words are:",c,)
    return r
    t.close()
    
def display():
     t=open("STORY.txt","r")
     c=0
     x=t.read()
     w=x.split()
     for i in w :
         if i[-1] in "?":
            c+=1
     r=print("total words are:",c,)
     t.close()

def length():
    f = open('STORY.txt',"r")
    f.read()
    d=f.tell()
    return d
    f.close()

def length5():
    t=open("STORY.txt","r")
    c=0
    x=t.read()
    w=x.split()
    for i in w :
        if len(i)==5:
            print(i)
    r=print("finish")
    return r
    t.close()

while True:
    z=int(input("enter the serial nnumber of the proframme:"))
    if z==0:
        print("thank you")
        break
    if z==1:
        print(count())
    if z==2:
        print(countl())
    if z==3:
        print(ch())
    if z==4:
        print(countv())
    if z==5:
        print(display())
    if z==6:
        print(length())
    if z==7:
        print(length5())
        
        

    
