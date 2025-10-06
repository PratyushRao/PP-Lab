#WAP to print factorial of a given number

def fact(n: int):
    if n==0:
        return 1
    return n*fact(n-1)

print(fact(5))