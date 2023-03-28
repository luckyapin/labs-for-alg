import random


#кубик нижняя грань 4 на 2, высота - 3,
X=2
Y=3
Z=4

array=[[[random.randint(1,10) for _ in range(Z)] for _ in range(Y)] for _ in range(X)]


print(array)
