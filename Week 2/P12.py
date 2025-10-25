#Check characters but do nothing with digits
text = "python123"
for char in text:
    if char.isdigit():
        pass
    else:
        print("letter: ",char)