L = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]

k=[]
for i in L:
    if i!=():
        k.append(i)
print(k)