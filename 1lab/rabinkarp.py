def RabinKarp(string, pattern):
    n, m = len(string), len(pattern)    
    count=0
    hpattern = hash(pattern)    
    for i in range(n-m+1):
            hs = hash(string[i:i+m])        
            if hs == hpattern:
                if string[i:i+m] == pattern:                
                    count+=1
    return count