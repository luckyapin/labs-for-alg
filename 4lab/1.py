from random import randint

def cell(reachable, summa=0, stuff =[]):
    return {
        "reachable": reachable,
        "summa": summa,
        "stuff": stuff
    } if reachable else {"reachable": reachable}

def backpack(m, k, exhibits):
    for i in range(m):
        weight = k
        dp = [[cell(False) for _ in range(weight + 1)] for _ in range(len(exhibits) + 1)]
        dp[0][0] = cell(True,0, [])
        for i in range(1, len(exhibits)+1):
            for j in range(weight + 1):
                if j-exhibits[i-1][1] >= 0:
                    if dp[i-1][j]["reachable"] and dp[i-1][j-exhibits[i-1][1]]["reachable"]:
                        dp[i][j] = cell(True,
                                        dp[i-1][j]["summa"]
                                        if (dp[i-1][j-exhibits[i-1][1]]["summa"] + exhibits[i-1][0]) < dp[i-1][j]["summa"]
                                        else (dp[i-1][j-exhibits[i-1][1]]["summa"]) + exhibits[i-1][0],
                                        dp[i - 1][j]["stuff"]
                                        if (dp[i - 1][j - exhibits[i - 1][1]]["summa"] + exhibits[i - 1][0]) < dp[i - 1][j][
                                            "summa"]
                                        else (dp[i - 1][j - exhibits[i - 1][1]]["stuff"]) + [exhibits[i - 1]])
                    elif dp[i-1][j]["reachable"]:
                        dp[i][j] = cell(True, dp[i-1][j]["summa"], dp[i-1][j]["stuff"])
                    elif dp[i-1][j-exhibits[i-1][1]]["reachable"]:
                        dp[i][j] = cell(True, (dp[i-1][j-exhibits[i-1][1]]["summa"]) + exhibits[i-1][0], dp[i-1][j-exhibits[i-1][1]]["stuff"] + [exhibits[i-1]])
                    else:
                        dp[i][j] = cell(False)
                else:
                    if dp[i-1][j]["reachable"]:
                        dp[i][j] = cell(True, dp[i-1][j]["summa"],dp[i-1][j]["stuff"])
                    else:
                        dp[i][j] = cell(False)
        ans = cell(True, 0, [])
        for j in range(weight+1):
            if ('summa' in dp[len(exhibits)][j].keys()):
                if (dp[len(exhibits)][j]["summa"]> ans["summa"]):
                    ans = dp[len(exhibits)][j]
        for l in range(len(ans["stuff"])):
            exhibits.remove(ans["stuff"][l])
        print(ans)






if __name__ == "__main__":
    exhibits = []
    N = 10  # количество экспонатов
    M = 3  # количество заходов
    K = 8  # кг веса
    for i in range(N):
       exhibits.append([randint(1,1000),randint(1,K)]) #стоимость, вес

    print("Ответ:")
    backpack(M,K,exhibits)



