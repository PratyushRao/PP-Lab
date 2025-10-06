#Simple Calculator
def calc(a: int, op: str, b: int) :
    if op=='+':
        return a+b
    elif op=='-':
        return a-b
    elif op=='/':
        return a/b
    elif op=='*':
        return a*b
    elif op=='//':
        return a//b
    elif op=='%':
        return a%b
    


a = int(input('Enter first number: '))
op = input("Enter Operator: ")
b = int(input('Enter second number: '))

print(a,op,b,'=',calc(a,op,b),sep=" ")
