#WAP to convert alternate characters in a string to capital letters

s = input("Enter a string: ")
sn=""
for i in range(len(s)):
    if(i%2==0):
        sn+=s[i].upper()
        continue
    sn+=s[i]
print(sn)