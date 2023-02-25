def naive(s):
    
    sl={}
    for i in range(len(s)-1):
        if s[i:i+2] in sl:        
            sl[s[i:i+2]]+=1
        else:        
            sl[s[i:i+2]]=1
    return sl



