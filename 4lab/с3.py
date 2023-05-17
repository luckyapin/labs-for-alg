blocks=[(3,3,10),(1,4,11),(1,1,5),(1,1,5)]
towers=[]

for i in range(len(blocks)):
    c=0
    if c==len(towers):
        towers.append([])
    
    if len(towers[c])==0:
        towers[c].append(blocks[i])
    else:
        while c != len(towers):
            for j in range(len(towers[c])):
                if blocks[i][0]<=towers[c][j][0] and blocks[i][1]<=towers[c][j][1]:
                    if j>0:
                        if blocks[i][0]>=towers[c][j-1][0] and blocks[i][1]>=towers[c][j-1][1]:
                            towers[c].insert(j, blocks[i])
                            c+=1
                            break
                    else:
                        towers[c].insert(j, blocks[i])
                        c+=1
                        break
            else:
                if blocks[i][0]>=towers[c][j][0] and blocks[i][1]>=towers[c][j][1]:
                    towers[c].append(blocks[i])
                    c+=1
                else:
                    c+=1
                    if c==len(towers):
                        towers.append([])
                        towers[c].append(blocks[i])
                        c+=1
        
print(towers)

mx=0
for i in towers:
    c=0
    for j in i:
        c+=j[2]
        mx=max(c,mx)
print(mx)