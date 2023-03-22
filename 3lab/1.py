def min_coins(n, coins):
    coins = dict(sorted(coins.items(), reverse=True))  # сортируем монеты по убыванию номинала
    result = []
    for coin in coins:  # жадный алгоритм
        while n >= coin and coins[coin] > 0:
            n -= coin
            coins[coin] -= 1
            result.append(coin)
    if n > 0:
        return None  # не удалось набрать сумму
    return result


n = 10
coins = {1: 1, 3: 3, 5: 2, 8: 1}  # номинал: количество
result = min_coins(n, coins)
if result is None:
    print("Невозможно набрать нужную сумму")
else:
    print("Минимальная комбинация монет:", *result)
