nums=input("enter the list of integers (separated within space):").split()
result=[]
for n in nums:
    n=int(n)
    if n>100 :
        result.append("over")
    else:
        result.append(n)
print (result)
