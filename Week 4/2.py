#Read a char from user & check if its a vowel or consonent. Print vowel/ consonent

ch = input("Enter a char: ")

if ch in "aeiouAEIOU":
    print("It is a vowel")
elif ch.isalpha(): 
    print("It is a consonant")

else:
    print("Invalid Input")