#Program to find the multiplication table
a=int(input("Enter a number:"))
n=int(input("Times to multiplied:"))
for i in range(1,n+1):
    print(a,"x",i,"=",i*a)
    