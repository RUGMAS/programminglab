#Count the occurrences of each word in a line of text.
r=input("Enter a text:\n").split()
a=list(set(r))
for i in a:
    print(i,"-",r.count(i))
