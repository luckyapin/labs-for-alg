import random
from shapely.geometry import Polygon

#создание четырехугольников (координаты)
N = int(input("Введите количество четырехугольников: "))
ch = [[] for _ in range(N)]
for i in range(N):
    tochka = set()
    while len(ch[i])!=4:
        x,y = random.randint(1,100), random.randint(1,100)
        if (x,y) not in tochka:
            ch[i].append((x,y))
        tochka.add((x, y))

print(Polygon(ch[1]).intersects(Polygon(ch[2])))


