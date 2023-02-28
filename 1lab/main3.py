import random
from shapely.geometry import LineString



#создание четырехугольников (координаты)
N = int(input("Введите количество четырехугольников: "))
ch = [[] for _ in range(N)]
i = 0
while i<N:
    tochka = set()
    while len(ch[i])!=4:
        x,y = random.randint(1,100), random.randint(1,100)
        if (x,y) not in tochka:
            ch[i].append((x,y))
        tochka.add((x, y))
    A = LineString([ch[i][0], ch[i][1]])
    B = LineString([ch[i][1], ch[i][2]])
    C = LineString([ch[i][2], ch[i][3]])
    D = LineString([ch[i][3], ch[i][0]])
    if not ((A.intersects(C) == False) and (B.intersects(D) == False)):
        ch[i]=[]
    else:
        ch[i] = [A, B, C, D]
        i+=1

stroka = ""
sl={0: 'A', 1: 'B', 2: 'C', 3: 'D'}
for i in range(N):
    for j in range(i+1,N):
        l=""
        for storona1 in range(4):
            for storona2 in range(4):
                if ch[i][storona1].intersects(ch[j][storona2]):
                    l+=(sl[storona1]+sl[storona2])
        stroka += l
        print(f"Пересечения {i+1} и {j+1} четырехугольника: {l}")


print(stroka)


