def cell(reachable, coins=[]):
    return {
        "reachable": reachable,
        "coins": coins
    } if reachable else {"reachable": reachable}

def backpack(n, coins):
    sum = n
    dp = [[cell(False) for _ in range(sum+1)] for _ in range(len(coins) + 1)]
    dp[0][0] = cell(True, [])
    for i in range(1, sum+1):
        dp[0][i] = cell(False)
    for i in range(1, len(coins)+1):
        for j in range(sum+1):
            if j-coins[i-1] >= 0:
                if dp[i-1][j]["reachable"] and dp[i-1][j-coins[i-1]]["reachable"]:
                    dp[i][j] = cell(True,
                                    dp[i-1][j]["coins"]
                                    if len(dp[i-1][j-coins[i-1]]["coins"])+1 > len(dp[i-1][j]["coins"])
                                    else (dp[i-1][j-coins[i-1]]["coins"]) + [coins[i-1]])
                elif dp[i-1][j]["reachable"]:
                    dp[i][j] = cell(True, dp[i-1][j]["coins"])
                elif dp[i-1][j-coins[i-1]]["reachable"]:
                    dp[i][j] = cell(True, (dp[i-1][j-coins[i-1]]["coins"]) + [coins[i-1]])
                else:
                    dp[i][j] = cell(False)
            else:
                if dp[i-1][j]["reachable"]:
                    dp[i][j] = cell(True, dp[i-1][j]["coins"])
                else:
                    dp[i][j] = cell(False)
    return dp[len(coins)][sum]





n = 10
m1, s1 = 1, 1 #количесвто, номинал
m2, s2 = 3, 3
m3, s3 = 2, 5
m4, s4 = 1, 8
coins = [s1]*m1+[s2]*m2+[s3]*m3+[s4]*m4
print(f"Ответ: {backpack(n,coins)}")

