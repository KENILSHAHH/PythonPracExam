num = [10,20,30,(10,20),40]
ctr = 0
for n in num:
    if type(n)==type(tuple()):
        break
    ctr += 1
print(ctr)
