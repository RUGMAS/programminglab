#To create a string from a given string where 1st of last character is exchanged.

word=(input("Enter a String:\n"))
F= word[0]
I= word[-1]
Mid =word[1:-1]
print(I+Mid+F)
