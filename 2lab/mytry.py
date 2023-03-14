def hashing(a):
    s=0
    m=256
    for i in a:
        s+=ord(i)
    hash=s%m
    
    return finding(hash,a)


def finding(hash,a):
    while hashtable[hash]:
        if hashtable[hash]==a:
            break
        hash=(hash+1)%256
    hashtable[hash]=a
    return hash
    

m=256
hashtable=[0]*m

print(hashing('ABCDEF'))
print(hashing('ABCDEF'))
print(hashing('ABCDFE'))
print(hashing('DDDCCC'))

print(hashtable)

line=hashing('ABCDEF')