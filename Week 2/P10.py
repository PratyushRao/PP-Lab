items= ["milk","bread","Out of Stock","butter"]
for item in items: 
    if item=="Out of Stock":
        continue
    print("Adding to cart: ", item)