#Password Retry System
attempts = 0
while attempts<3:
    pwd = input("Enter Password: ")
    if pwd == "Python123":
        print("Access Granted!!")
        break
    else:
        print("Try Again!!")
    attempts+=1


if (attempts>=3):
    print("Too many incorrect attempts!!!")