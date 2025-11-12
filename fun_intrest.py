def calculate(p,n,r):
    s=(p*n*r)/100
    print("simplest interest=",s)
age=int(input("enter the age: "))
p=int(int(input("enter the principal amount:")))
n=int(input("enter the number of years:"))
if age<60:
        r=10

else:
        r=12
        print("rate of interest:",r)
        calculate(p,n,r)