s=open("sample.txt","w")
n=int(input("enter the number of lines to be printed:"))
for i in range(0,n):
    t=str(input("enter:"))
    s.write(t)
    s.write("\n")
s.close()
print("created by saiyam jain")
