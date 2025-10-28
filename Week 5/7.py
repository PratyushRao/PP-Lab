def is_palindrome(word: str):
    return word==word[::-1]

print(is_palindrome("malayalam"))