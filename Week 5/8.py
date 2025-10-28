def apply_discount(price, discount_percent):
    return (1-discount_percent/100)*price


print(apply_discount(10000,4.79))