l = [3,4,6,2,0,0,0,0,0,0,6,7,6,9,10,0,0,0,0,0,7,4,4,0,0,0,0,0,0,5,3,2,9,7,1,0,0,0]
k=[]
sum=0
for i in l:
    if i!=0:
        sum+=i
    else:
        if sum>0:
            k.append(sum)
        sum=0
print(k)
