def count_vowels(word: str):
    vowels = "aeiouAEIOU"
    cnt=0
    for char in word:
        if char in vowels:
            cnt+=1
            print(char)
    return cnt

l = ['Hi', 'Hello', 'welcome']

for i in range(len(l)):
    print("word: ", l[i])
    cnt= count_vowels(l[i])
    print(cnt, " vowels")
    print()
