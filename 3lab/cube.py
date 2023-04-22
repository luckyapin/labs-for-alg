import random
def sr(i,j,k):
    
    mn=float('inf')
    ind=(0,0,0)
    if i-1>=0:
        
        mn=rez[i-1][j][k]
        ind=(i-1,j,k)

    if j-1>=0:
        
        if mn>rez[i][j-1][k]:
            mn=rez[i][j-1][k]
            ind=(i,j-1,k)
        
        
    if k-1>=0:
        if mn>rez[i][j][k-1]:
            mn=rez[i][j][k-1]
            ind=(i,j,k-1)

    if i!=0 or j!=0 or k!=0:
        
        path[','.join([str(i),str(j),str(k)])]=','.join(list(map(str,ind)))
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
            arr[i][j].append(random.randint(1,100))
            rez[i][j].append(float('inf'))
for i in range(x):
    print()
    for j in range(y):
        print(*arr[i][j])

rez[0][0][0]=arr[0][0][0]
path={}
i=j=k=0
for i in range(x):
    for j in range(y):
        for k in range(z):
            
            sr(i,j,k)
            
a='2,2,2'
rezpath=[a]

while a!='0,0,0':
    a=path[a]
    rezpath.append(a)

print('Путь: ',list(reversed(rezpath)))
print('Итоговая сумма: ', rez[x-1][y-1][z-1])