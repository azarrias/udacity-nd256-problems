"""
Knapsack Problem
Maximize value of items that we can fit in a theoretical Knapsack.
Given an associated weight and value for each item and maximum weight
capacity for the knapsack.
Store and reuse the intermediate results in a lookup table. This step 
is called memoization. Start with initializing a lookup table (a list), 
where the index represents the remaining capacity (kg) of the knapsack, 
and the element represents the maximum value ($) that it can hold.
For a given item, if the item-weight is less than the remaining 
capacity (kg) of the knapsack, then we have two options:
 - Do not pick the item - In this case, the value ($) of knapsack with 
   the remaining capacity would not change. It can be represented as 
   lookup_table[capacity].
 - Pick the item - In this case, the value ($) and capacity (kg) of 
   the knapsack would be updated. The value ($) of the knapsack will be 
   equal to value ($) of the current object + value ($) in the lookup 
   table at [capacity - item.weight] position. It can be represented as 
   lookup_table[capacity - item.weight] + item.value.
Update the lookup table, lookup_table[capacity], with the maximum of 
either of the above two values.
Note - This approach with dynamic programming will have a time 
complexity as O(nC), where n is the number of given items and C is the 
max capacity (kg) of the knapsack. 
"""

# Helper code
import collections
# An item can be represented as a namedtuple
Item = collections.namedtuple('Item', ['weight', 'value'])

def knapsack_max_value(max_weight, items):
    """
    Get the maximum value of the knapsack.
    """
    # Initialize a lookup table to store the maximum value
    lookup_table = [0] * (max_weight + 1)

    # Iterate down the given list
    for item in items:
        # The capacity represents amount of remaining capacity of the
        # knapsack at a given moment
        for capacity in reversed(range(max_weight + 1)):
            if item.weight <= capacity:
                lookup_table[capacity] = max(lookup_table[capacity], lookup_table[capacity - item.weight] + item.value)

    return lookup_table[-1]

if __name__ == '__main__':
    tests = [
        {
            'correct_output': 14,
            'input':
                {
                    'max_weight': 15,
                    'items': [Item(10, 7), Item(9, 8), Item(5, 6)]}},
        {
            'correct_output': 13,
            'input':
                {
                    'max_weight': 25,
                    'items': [Item(10, 2), Item(29, 10), Item(5, 7), Item(5, 3), Item(5, 1), Item(24, 12)]}}]
    for test in tests:
        if test['correct_output'] == knapsack_max_value(**test['input']):
            print("Pass")
        else:
            print("Fail")