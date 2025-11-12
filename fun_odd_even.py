def check(n):
    if n%2==0:
        return("it is even")

    else:
        return("it is odd")

num=int(input("enter the number:"))
print("the given number is",num,check(num))
