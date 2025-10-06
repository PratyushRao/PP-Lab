def isLeap(yr):
    if ((yr%100!=4 and yr%4==0) or (yr%100==0 and yr%400==0)):
        return True
    return False

lyr= [1998, 1996,2000,1900,1567]

for i in range(len(lyr)):
    if isLeap(lyr[i]):
        print(lyr[i], end = " ")
print()