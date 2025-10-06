#WAP to read a sentence & print the longest word in that sentence

s=input("Enter a sentence: ")

l = s.split()

max, maxl = l[0], len(l[0])
for i in l:
    if len(i)>maxl:
        maxl=len(i)
        max=i
print(max,"has maximum length")