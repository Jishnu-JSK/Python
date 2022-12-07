#Four Number Calculator
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=[a+b,a-b,a*b,a/b,a//b]
d=int(input('''Menu 1
ADD 0
SUB 1
MULTI 2
DIVIDE(Floor) 3
DIVIDE(Integer) 4
Enter your choice:
'''))
e=c[d]
f=int(input("Enter third number:"))
g=int(input("Enter fourth number:"))
h=[f+g,f-g,f*g,f/g,f//g]
i=int(input('''Menu 2
ADD 0
SUB 1
MULTI 2
DIVIDE(Floor) 3
DIVIDE(INTEGER) 4
Enter your choice:
'''))
j=h[i]
z=input('''Enter the operation to combine the four numbers:
ADD 
SUB
MULTI
FLOOR
INT
Enter your choice:
''')
if z in ["ADD","Add","add"]:
    x=e+j
    print("Output:",x)
elif z in ["SUB","Sub","sub"]:
    y=e-j
    print("Output:",y)
elif z in ["MULTI","Multi","multi"]:
    w=e*j
    print("Output:",w)
elif z in ["FLOOR","Floor","floor"]:
    l=e/j
    print("Output:",l)
elif z in ["INT","Int","int"]:
    q=e//j
    print("Output:",q)
else:
    pass
