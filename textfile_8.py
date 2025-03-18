s=open("s1.txt","w+")
r=int(input("how mny lines to be printed: "))
for i in range(0,r):
    o=str(input("enter the line:"))
    s.write(o)
    s.write('/n')
s.close()
