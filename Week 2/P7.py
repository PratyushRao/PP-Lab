#Stop when you find eraser (using break statement)
items = ["pen","notebook","marker","eraser"]
for item in items:
    if item == "eraser":
        print("Eraser found!")
        break
    print("Checking: ",item)