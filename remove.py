nums=list(map(int,input("enter the list of integers (separated by space):").split()))
result=[]
for n in nums:
    if n % 2!=0:
        result.append(n)
        print ("entered numbers :",nums)
        print("list after removing even numbers :", result)
