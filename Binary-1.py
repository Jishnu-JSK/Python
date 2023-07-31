import pickle
with open("emp.dat","ab") as e:
    d={}
    ch="y"
    while ch == "y" or ch == "Y":
        eno=int(input("Enter ENo:"))
        name=input("Enter the employees name:")
        salary=input("Enter the Salary:")

        d["Eno"]=eno
        d["Name"]=name
        d["Salary"]=salary

        pickle.dump(d,e)

        ch=input("Do you want to continue Y/N:")
