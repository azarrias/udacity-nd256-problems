"""
Coin Change

You are given coins of different denominations and a total amount of money. 
Write a function to compute the fewest coins needed to make up that amount. 
If that amount of money cannot be made up by any combination of the coins, 
return -1.

As an example:
    Input: coins = [1, 2, 3], amount = 6
    Output: 2
    Explanation: The output is 2 because we can use 2 coins with value 3. That 
    is, 6 = 3 + 3. We could also use 3 coins with value 2 (that is, 6 = 2 + 2 + 
    2), but this would use more coins—and the problem specifies we should use 
    the smallest number of coins possible.
"""

# recursive solution
# Let's assume F(Amount) is the minimum number of coins needed to make a change from coins [C0, C1, C2...Cn-1]
# Then, we know that F(Amount) = min(F(Amount-C0), F(Amount-C1), F(Amount-C2)...F(Amount-Cn-1)) + 1
def coin_change(coins, amount):
    # Use lookup table, to store the fewest coins for a given amount that have
    # been already calculated, to be able to use the result without having to
    # calculate it again
    lookup = {}

    def return_change(remaining):
        # Base cases
        if remaining < 0: 
            return float("Inf")
        if remaining == 0:
            return 0
        
        if remaining not in lookup:
            lookup[remaining] = min(return_change(remaining - coin) + 1 for coin in coins)
        return lookup[remaining]
    
    result = return_change(amount)
    if result == float("Inf"):
        return -1
    return result

# iterative solution
# We initiate F[Amount] to be float('inf') and F[0] = 0
# Let F[Amount] to be the minimum number of coins needed to get change for the Amount.
# F[Amount + coin] = min(F(Amount + coin), F(Amount) + 1) if F[Amount] is reachable.
# F[Amount + coin] = F(Amount + coin) if F[Amount] is not reachable.
def coin_change_iter(coins, amount):
    # initialize list with length amount + 1 and prefill with value 'Infinite'
    result = [float('Inf')] * (amount + 1)
    # when amount is 0, the result will be 0 coins needed for the change
    result[0] = 0

    i = 0
    while i < amount:
        if result[i] != float('Inf'):
            for coin in coins:
                if i <= amount - coin:
                    result[i+coin] = min(result[i] + 1, result[i + coin])
        i += 1

    if result[amount] == float('Inf'):
        return -1
    return result[amount]

def test_function(test_case, fn):
    arr = test_case[0]
    amount = test_case[1]
    solution = test_case[2]
    output = fn(arr, amount)
    print(output)
    if output == solution:
        print("Pass")
    else:
        print("Fail")

if __name__ == '__main__':
    print("- Test recursive solution")

    # Test case 1
    arr = [1,2,5]
    amount = 11
    solution = 3
    test_case = [arr, amount, solution]
    test_function(test_case, coin_change)

    # Test case 2
    arr = [1,4,5,6]
    amount = 23
    solution = 4
    test_case = [arr, amount, solution]
    test_function(test_case, coin_change)

    # Test case 3
    arr = [5,7,8]
    amount = 2
    solution = -1
    test_case = [arr, amount, solution]
    test_function(test_case, coin_change)

    print("- Test iterative solution")

    # Test case 1
    arr = [1,2,5]
    amount = 11
    solution = 3
    test_case = [arr, amount, solution]
    test_function(test_case, coin_change_iter)

    # Test case 2
    arr = [1,4,5,6]
    amount = 23
    solution = 4
    test_case = [arr, amount, solution]
    test_function(test_case, coin_change_iter)

    # Test case 3
    arr = [5,7,8]
    amount = 2
    solution = -1
    test_case = [arr, amount, solution]
    test_function(test_case, coin_change_iter)
