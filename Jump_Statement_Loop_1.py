a=int(input("Enter a number:"))
b=int(input("Enter a conditional number:"))
n=int(input("Times to be Looped:"))
for a in range(n):
    a+=1
    if a==b:
        break
    print("Value",a)
print("Out of the Loop")
