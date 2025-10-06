l=[ 12,23,22,34,5,66,76]

def track_expenses(l: list) :
    sum=0
    for i in l:
        sum+=i
    return sum,sum/len(l)

print("Total Amount: ", track_expenses(l)[0],"   Average Expense: ", track_expenses(l)[1])