#Get a string from an input string where all occurrences of first character replaced with
#‘$’, except for the first character.

x=str(input("Enter the String:\n"))
a=x[0]
for i in x:
 if(i==a):
     x=x.replace(i,"$")
     x=a+x[1:]
     print(x)
