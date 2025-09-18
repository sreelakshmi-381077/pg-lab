list1=input("enter the colors in list1(separated within space):").split()
list2=input("enter the colors in list2(separated within space):").split()
result=[]
for color in list1:
    if color not in list2:
        result.append(color)
print(result)