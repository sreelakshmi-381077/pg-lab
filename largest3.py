a=int(input("enter first number:"))
b=int(input("enter second number: "))
c=int(input("enter third number: "))
if a>b:
    if a>c:
        print("The biggest number is:",a)
    else:
        print("The biggest number is:", c)
else:
    if b>c:
          print("The biggest number is:", a)
    else:
        print("The biggest number is:", c)

