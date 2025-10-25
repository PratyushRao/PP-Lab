#Check for valid input
scores = [85,90,76,-10,95]
for score in scores:
    if score<0 or score>100:
        print("Invalid score: Upload stopped")
        break
    print("Valid Score", score)