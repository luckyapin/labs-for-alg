import random
n=20
array=[random.randint(-100,100) for i in range(n)]
print(array)
c=1
mx=float('-inf')
for i in range(len(array)-1):

    if array[i+1]>array[i]:
        c+=1
    else:
        c=1
    mx=max(c,mx)
print(mx)
    
