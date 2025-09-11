text=input("enter a string:")
if(len(text)<2):
    result=text
else:
    result=text[-1]+text[1:-1]+text[0]
print("Result:",result)

