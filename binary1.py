#store an display multiple integer
import pickle
f=open("integer.dat","wb")
n=int(input("enter the number of terms to be added in the file:"))
for i in range(0,n):
      x=int(input("enter the number:"))
      pickle.dump(x,f)
f.close()
print("the data is updted")
s=open("integer.dat","rb")
try:
    while True:
        print(pickle.load(s))
except EOFError:
    pass
