def division_alg(keys):
    length=len(keys)
    while True: #тут мы ищем простое
        if prime(length):
            break
        length+=1
    
    return [x % length for x in keys]


def prime(lenght): #на сайте написано, что число должно быть простым
    d=2
    while d*d<=lenght:
        if lenght % d ==0:
            return False
        d+=1
    return True
    
keys=[25,19,7,34,16,61,44,81]
print(division_alg(keys))
