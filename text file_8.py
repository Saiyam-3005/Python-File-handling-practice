def file_long(name):
    t=open(name)
    l=""
    for i in t:
        if len(i)>=len(l):
            l=i
    return l
name=str(input("enter the name of the file in txt format :"))
print(file_long(name))
