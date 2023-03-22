M = 4  # кол-о заходов
K = 20  # вместимось рюкзака вора (кг)

# спискок экспонатов: название, вес (кг), цена
prod = {
    'голова зверя': [12, 10_000],
    'китайская статуя': [20, 5_000],
    'ложка царя': [2, 20_000],
    'картина': [13, 9_000],
    'чемодан': [40, 6_000],
}

N = len(prod)  # кол-о экспонатов

# вичислим ценность экспонатов (цена/кг)
prod_val = {}
for i in prod.keys():
    val = prod[i][1] / prod[i][0]
    prod_val[i] = val

# отсортируем по убыванию ценности
prod_sort = sorted(prod_val.items(), key=lambda x: x[1], reverse=True)
dict(prod_sort)

# используем жадный алгоритм, выбираем товары
mine = {}  # храним товары, вес и стоимость

for k in range(M):
    weight = 0  # текущий вес захода
    count = 0  # счетчик, чтобы не уходить в бесконечный цикл

    while weight < K and len(prod_sort) != 0 and count == 0:
        pop_num = []  # индексы товаров, которые нужно удалить (ибо их взяли)
        for i in range(len(prod_sort)):
            count = 1
            # проверка, добавление, удаление
            if prod[prod_sort[i][0]][0] + weight <= K:
                mine[prod_sort[i][0]] = prod[prod_sort[i][0]]
                weight += prod[prod_sort[i][0]][0]
                pop_num.append(i)

        print(f"Взяли - {mine}, Вес захода - {weight}, Номер захода - {k + 1}")
        for num in pop_num:
            prod_sort.pop(num)

# вывод
print('\n'
      'Итого: '
      f"{mine}\n"
      'Стоимость: '
      f"{sum([prod[i][1] for i in mine.keys()])} руб\n"
      'Вес: '
      f"{sum([prod[i][0] for i in mine.keys()])} кг"
      )

