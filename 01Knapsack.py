
"""
0-1 Knapsack

Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack. 
In other words, given two integer arrays val[0..n-1] and wt[0..n-1] which represent values and weights associated with n items respectively. 
Also given an integer W which represents knapsack capacity, find out the maximum value subset of val[] such that sum of the weights of this subset 
is smaller than or equal to W. You cannot break an item, either pick the complete item or don’t pick it (0-1 property)

"""

# Recursion
def knapsack(index,weights,val,capacity):

    # Base Case
    # Starting from n-1 -> 0 when we are at the last index ie 0 we need to check if we can take the weight or not
    if index == 0:
        if weights[0] <= capacity:
            return val[0]
        else:
            return 0

    not_take = knapsack(index-1,weights,val,capacity)

    take = -100

    if weights[index] <= capacity:
        take = val[index] + knapsack(index-1,weights,val,capacity-weights[index])

    return max(take,not_take)




def main():

    wt = list()
    val = list()

    n = int(input("Enter total number of weights"))

    print("Enter weights")
    for i in range(0,n):
        weight = int(input())
        wt.append(weight)

    print("Enter values")
    for i in range(0,n):

        values = int(input())
        val.append(values)
    
    W = int(input("Enter Capacity"))

    print(knapsack(n-1,wt, val, W))   




if __name__ == "__main__":
    main()




"""
Dynamic Programming

"""

# Memoization
# Time Complexity : O(N*Capacity)
# Space Compexity : O(N*Capacity) + O(N)

def knapsack(index,weights,val,capacity,dp):

    # Base Case
    if index == 0:
        if weights[index] <= capacity:
            return val[0]
        else:
            return 0

    if dp[index][capacity] != -1:
        return dp[index][capacity]

    not_take = knapsack(index-1,weights,val,capacity,dp)

    take = -100

    if weights[index] <= capacity:
        take = val[index] + knapsack(index-1,weights,val,capacity-weights[index],dp)

    dp[index][capacity] = max(take,not_take)
    return dp[index][capacity]
    
    
def main():

    wt = list()
    val = list()

    n = int(input("Enter total number of weights"))

    print("Enter weights")
    for i in range(0,n):
        weight = int(input())
        wt.append(weight)

    print("Enter values")
    for i in range(0,n):

        values = int(input())
        val.append(values)
    
    W = int(input("Enter Capacity"))

    rows,cols = (n,W+1)
    dp = [[-1]*cols]*rows

    
    print(knapsack(n-1,wt, val, W,dp))   



if __name__ == "__main__":
    main()



