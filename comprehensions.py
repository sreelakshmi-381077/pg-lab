numbers= [-3,5,-1,8,0,-4]
print("Given inputs is",numbers)
positive_list=[num for num in numbers if num>0]
squares=[num **2 for num in positive_list]
print("postive numbers",positive_list)
print("squares",squares)
words=input("enter some words:")
vowels='aeiouAEIOU'
vowels_list=[char for char in words]
print("Vowels in the word:",vowels_list)
ordinal_values=[ord(char)for char in words]
print("Ordinal values of each character:",ordinal_values)