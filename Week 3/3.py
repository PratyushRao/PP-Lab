def count_vowels(word: str):
    vowels = "aeiouAEIOU"
    cnt=0
    for char in word:
        if char in vowels:
            cnt+=1
    print("Number of vowels in ",word," is ", cnt)


count_vowels("education")