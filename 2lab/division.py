def division_alg(keys):
    M=len(keys)
    while True: 
        if prime(M):
            break
        M+=1
    
    return [i % M for i in keys]


def prime(M): 
    d=2
    while d*d<=M:
        if M % d ==0:
            return False
        d+=1
    return True

line='hello world!'
keys=[ord(i) for i in line]
print('line: ', line)
print('keys: ', keys)
print('hash: ',division_alg(keys))
