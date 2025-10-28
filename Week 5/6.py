def calculate_salary(hours_worked, hourly_rate, bonus=0):
    return hours_worked*hourly_rate + bonus

print(calculate_salary(20,100,2))