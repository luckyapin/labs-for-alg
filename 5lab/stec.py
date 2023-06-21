def add(element, number):
    flag=False
    for i in range(len(stec)-1, 0-1, -3):
        place=i-number+1
        if stec[place]!=0 and flag:
            stec[place+3]=element
            break
        elif stec[place]==0:
            flag=True
        elif stec[place]!=0 and not flag:
            stec.append(0)
            stec.append(0)
            stec.append(0)
            stec[place+3]=element
            break
    else:
        stec[place]=element
        
    print(stec)


def delete(number):
    for i in range(len(stec)-1, 0-1, -3):
        place=i-number+1
        if stec[place]!=0:
            a=stec[place]
            stec[place]=0
            print(stec)
            return a
        
    
stec=[0, 0, 0 ]
add(1,1)
add(2,1)
add(3,1)
add(1,2)
add(2,2)
add(1,3)
add(3,2)
add(2,3)

delete(3)
delete(2)
delete(3)
delete(1)
delete(1)
delete(1)
delete(1)
