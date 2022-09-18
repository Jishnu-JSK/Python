a=float(input("Enter First number:"))
b=float(input("Enter Second number:"))
c=[a+b,a-b,a*b,a/b]
d=int(input('''a+b 0
a-b 1
a*b 2
a/b 3 
Choose an operator:'''))
e=c[d]
f=float(input("Enter Third number:"))
g=float(input("Enter Fourth number:"))
op=input("Enter an Operator:")
if op == "+": 
    print(e+f+g)
elif op == "-":
    print(e-f-g)
elif op == "*":
    print(e*f*g)
elif op == "/":
    print(e/f/g)
else: 
    print("Invalid Operator") 
    