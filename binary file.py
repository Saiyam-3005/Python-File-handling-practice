#appending data in  the binary file
import pickle
f=open("integer.dat","ab")
n=int(input("enter the number of terms to be added in the file:"))
for i in range(0,n):
      x=str(input("enter the content :"))
      pickle.dump(x,f)
f.close()
print("file updated")

