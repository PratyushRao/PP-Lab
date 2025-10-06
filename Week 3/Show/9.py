def rev(s):
    return s[::-1]
l = ["Hello", "Hi", "Prats"]


for i in range(len(l)):
    l[i] = rev(l[i])

print(l)