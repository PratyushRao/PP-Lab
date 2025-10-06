#Traffic Signal
col = input ("Enter colour: ")

if col.lower()=='red':
    print("STOP")

elif col.lower()=='green':
    print('GO')

elif col.lower() == 'yellow':
    print("CAUTION")

else:
    print("Enter valid input!!!")