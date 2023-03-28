def sr(i,j,k):
    mn=float('inf')
    if i-1>=0:
        
        mn=rez[i-1][j][k]
    elif j-1>=0:
        
        
        mn=min(mn,rez[i][j-1][k])
    elif k-1>=0:
        
        
        mn=min(mn,rez[i][j][k-1])
    if i!=0 or j!=0 or k!=0:
        rez[i][j][k]=arr[i][j][k] + mn
arr=[]
x=3
y=3
z=3
rez=[]
for i in range(x):
    arr.append([])
    rez.append([])
    for j in range(y):
        arr[i].append([])
        rez[i].append([])
        for k in range(z):
            arr[i][j].append(1)
            rez[i][j].append(0)

print(arr)
rez[0][0][0]=arr[0][0][0]

i=j=k=0
for i in range(x):
    for j in range(y):
        for k in range(z):
            
            sr(i,j,k)
            
    
            
print(rez)
print('итоговая сумма: ', rez[x-1][y-1][z-1])