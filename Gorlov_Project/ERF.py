def erf(y1,y2):
    s=0
    for i in range(len(y1)):
        s+=(y2[i]-y1[i])**2
    return s/len(y1)

