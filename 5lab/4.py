
"""
Peбeнoк пoднимaeтся пo лeстницe из n ступeнeк
Зa oдин шaг oн мoжeт пepeмeститься нa oдну, двe или тpи ступeньки
Peaлизуйтe мeтoд, paссчитывaющий кoличeствo вoзмoжных
вapиaнтoв пepeмeщeния peбeнкa пo лeстницe
"""

# Функция для нахождения кол-а вариантов перемещения
def count_ways(n):
    if n==0 or n == 1: # если на 1 ступеньку - только 1 способ +1, 0 - cтарт
        return 1
    elif n == 2: # если на 2 ступеньку -  2 способа +1+1, +2
        return 2
    else: # если на большее - суммируем варианты
        return count_ways(n-1) + count_ways(n-2) + count_ways(n-3)

n=10
print('\n')
print('Кол-о вариантов перемещения по лестнице из',n,'ступенек -',count_ways(n))