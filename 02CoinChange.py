
"""
Problem : Coin Change

You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
You may assume that you have an infinite number of each kind of coin.

Input: coins = [1,2,5], amount = 11
Output : 3

"""
# Recursion
# TC : Exponential , SC: O(amount) -> worst case
def coinChange(index,coins,amount):

    if index == 0:
        if amount%coins[index] == 0:
            return amount/coins[0]
        else:
            return 10000

    not_take = coinChange(index-1,coins,amount)
    take = 10000

    if(amount >= coins[index]):
        take = 1 + coinChange(index,coins,amount-coins[index])

    return min(take,not_take)

def main():

    n = int(input("Enter the number of denominations of coins : "))
    coins = list()
    for i in range(0,n):
        c = int(input("Enter the Denominations"))
        coins.append(c)

    amount = int(input("Enter the total amount"))

    print(coinChange(n-1,coins,amount))

if __name__ == "__main__":
    main()
    



# Memoization
# TC : O(N*amount) , SC : O(N*amount) + O(amount)

def coinChange(index,coins,amount,dp):

    if index == 0:
        if amount%coins[index] == 0:
            return amount/coins[0]
        else:
            return 10000

    if dp[index][amount] != -1 : return dp[index][amount]


    not_take = coinChange(index-1,coins,amount,dp)
    take = 10000

    if(amount >= coins[index]):
        take = 1 + coinChange(index,coins,amount-coins[index],dp)

    dp[index][amount] = min(take,not_take)
    return dp[index][amount]

def main():

    n = int(input("Enter the number of denominations of coins : "))
    coins = list()
    for i in range(0,n):
        c = int(input("Enter the Denominations"))
        coins.append(c)

    amount = int(input("Enter the total amount"))

    rows,cols = (n,amount+1)
    dp = [[-1]*cols]*rows
    # print(dp)
    print(coinChange(n-1,coins,amount,dp))

if __name__ == "__main__":
    main()





# Tabulation
# TC : O(N*amount) , SC : O(N*amount)
def coinChange(n,coins,amount,dp):

    for t in range(0,amount+1):
        if t % coins[0] == 0:
            dp[0][t] = t/coins[0]
        else:
            dp[0][t] = 10000

    for i in range(0,n):
        for target in range(0,amount+1):
            not_take = dp[i-1][target]
            take = 10000

            if(target >= coins[i]):
                take = 1 + dp[i][target-coins[i]]

            dp[i][target] = min(take,not_take)
    return dp[n-1][amount]

def main():

    n = int(input("Enter the number of denominations of coins : "))
    coins = list()
    for i in range(0,n):
        c = int(input("Enter the Denominations"))
        coins.append(c)

    amount = int(input("Enter the total amount"))

    rows,cols = (n,amount+1)
    dp = [[-1]*cols]*rows
    # print(dp)
    print(coinChange(n,coins,amount,dp))

if __name__ == "__main__":
    main()


