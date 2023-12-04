def makeChange(coins, total):
    if total <= 0:
        return 0
    
    # Initialize an array to store the minimum number of coins needed for each total value
    # Initialize all values to be infinity, except for the total value of 0 which requires 0 coins
    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    
    # Iterate through each coin value
    for coin in coins:
        # Update the minimum number of coins needed for each total value
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    
    # If the value at the total index is still infinity, it means the total cannot be reached
    # Otherwise, return the minimum number of coins needed for the given total
    return dp[total] if dp[total] != float('inf') else -1

# Example usage:
coins = [1, 2, 5]
total = 11
result = makeChange(coins, total)
print(result)  # Output: 3 (since 11 = 5 + 5 + 1)
print(makeChange([1, 2, 25], 37))

print(makeChange([1256, 54, 48, 16, 102], 1453))
