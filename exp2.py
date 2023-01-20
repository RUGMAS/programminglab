#List comprehensions:
#(a) Generate positive list of numbers from a given list of integers
#(b) Square of N numbers
#(c) Form a list of vowels selected from a given word
#(d) List ordinal value of each element of a word (Hint: use ord() to get ordinal values)

a=[1,-3,7,55,78,-99,-101]
print("Positive integer \n")
c=[x for x in a if x>0]
d=[x**2 for x in a]
v=['a','e,','i','o','u']
k=input("Enter the string \n")
st=[x for x in k if x in v]
j=[ord(x) for x in k]
print("a- positive integers\n"+str(c))
print("\n b- squares\n"+str(st))
print("\n c- vowels\n"+str(st))
print("\n d- ordinal value \n"+str(j))
