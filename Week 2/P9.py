#Print marks but skip absentees (using continue statement)
marks =[45,50,"A",67,80]
for m in marks: 
    if m=="A":
        continue
    print("Scored: ",m)