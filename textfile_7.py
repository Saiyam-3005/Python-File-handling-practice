'''Write a menu driven programs to do the following tasks with the help of
user-defined functions
1) Write data to a text file
2) Read all data from a file using read()
3) Read all data from a file using readline()
4) Read all data from a file using readlines()
5) To find the size of file in bytes & no. of lines'''
print("by saiyam jain")
import os
print("FIRST CREATE A FILE :")
s=open("PRACTICLE.txt","w")
n=int(input("enter the number of lines to be printed:"))
for i in range(0,n):
    t=str(input("enter:"))
    s.write(t)
    s.write("\n")
s.close()
def write():
    t=open("PRACTICLE.txt","a")
    j=int(input("enter the number of lines to be printed:"))
    for i in range(0,j):
        l=str(input("enter:"))
        t.write(l)
        t.write("\n")
    t.close()
def read():
    t=open("PRACTICLE.txt","r")
    d=t.read()
    return d
    t.close()
    
def readlines():
    t=open("PRACTICLE.txt","r")
    l=t.readlines()
    for l1 in l:
        print(l1,end="\n")
    t.close()
def readline():
    t=open("PRACTICLE.txt","r")
    f=t.readline()
    while f:
        print(f)
        f=t.readline()
    t.close()
def size():
    f = open('PRACTICLE.txt',"r")
    f.read()
    d=f.tell()
    return d
    f.close()
def number():
    f = open('PRACTICLE.txt',"r")
    l=f.readlines()
    g=len(l)
    return g
print('MAIN MENU')
print('1.Write data to a text file')
print("2.Read all data from a file using read()")
print("3.Read all data from a file using readlines()")
print("4.Read all data from a file using readline()")
print("5.To find the size of file in bytes")
print("6.To find the s no. of lines")
k=1
while k==1:
    h=int(input("ENTER THE SERIAL NUMBER OF THE PROGRAMME TO BE RUN:"))
    if h==1:
        print(write())
        print("file successfully updated")
    if h==2:
         print(read())
    if h==3:
         print(readlines())
    if h==4:
       print(readline())
    if h==5:
         print(size())
    if h==6:
       print(number())
