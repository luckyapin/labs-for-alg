blocks=[(1,2,3),(2,3,1),(3,1,2),(2,1,3),(3,2,1)]
blocks = sorted(blocks, key=lambda b: b[1], reverse=True)
blocks = sorted(blocks, key=lambda b: b[0], reverse=True)
towers=[]
print(blocks)
for block in blocks:
    added=False
    for tower in towers:
        
        if block[0]>tower[-1][0] or block[1] > tower[-1][1]:
            
            continue
        tower.append(block)
        added=True
        
    if not added:
        towers.append([block])
print(towers)

mx=0
for i in towers:
    c=0
    for j in i:
        c+=j[2]
        mx=max(c,mx)
print(mx)