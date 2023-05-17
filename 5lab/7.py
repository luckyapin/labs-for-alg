
"""
Дaн нeoтсopтиpoвaнный мaссив цeлых чисeл.
Вepнитe нaимeньшee пpoпущeннoe цeлoe числo.
Aлгopитм дoлжeн выпoлняться зa вpeмя O(n)
"""

# Модуль чисел не превосходит 100
massiv=[10,12,32,2,2,343,1,4,5,53,32,4]

# Используя set и минимальное число (оно неизвестно)
def find_missing_number(massiv):
    num_set = set(massiv)
    min_num = min(massiv)
    while min_num in num_set:
        min_num += 1
    return min_num

print('Массив',massiv,'длиной',len(massiv))
print('Наименьшее пропущенное число -',find_missing_number(massiv))