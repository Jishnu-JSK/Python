import pickle
f=open("emp.dat","rb+")
try:
    while True:
        z=pickle.load(f)
        print(z)
except EOFError:
    pass
f.close()