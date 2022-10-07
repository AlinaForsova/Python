Array=[1,2,3,5,6,7]
delta=4
k=0
for i in range(1,len(Array)):
    if Array[i]-min(Array)==delta:
        k+=1
print(k)
