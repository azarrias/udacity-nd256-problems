"""
Longest Common Subsequence

In text analysis, it is often useful to compare the similarity of two texts 
(imagine if you were trying to determine plagiarism between a source and 
answer text). In this notebook, we'll explore one measure of text similarity, 
the Longest Common Subsequence (LCS).
  - The Longest Common Subsequence is the longest sequence of letters that 
    are present in both the given two strings in the same relative order.
Example - Consider the two input strings, str1 = 'ABCD' and str2 = 'AXBXDX'. 
The LCS will be 'ABD' with the length as 3 letters. It is because each of the 
letters 'A' , 'B', and 'D' are present in both the given two strings in the 
same relative order. Note that:
  - An LCS need not necessarily be a contiguous substring.
  - There can be more than one LCS present in the given two strings.
  - There can be many more common subsequences present here, with smaller 
    length. But, in this problem we are concerned with the longest common 
    subsequence.
"""

def lcs(string_a, string_b):
    """
    Calculate the length of the longest common subsequence of characters 
    between two strings. 
    The time complexity of this implementation is dominated by the two nested 
    loops, let the length of string_a and string_b is 'n' and 'm' respectively. 
    This would lead to a time complexity of O(n*m). 
    But in general, we can consider it as O(n*n) instead of O(n*m).
    """
    matrix = [[0 for i in range(len(string_a) + 1)] for j in range(len(string_b) + 1)]
    for y in range(1, len(string_b) + 1):
        for x in range(1, len(string_a) + 1):
            if string_a[x-1] == string_b[y-1]:
                matrix[y][x] = matrix[y-1][x-1] + 1
            else:
                matrix[y][x] = max(matrix[y-1][x], matrix[y][x-1])
    return matrix[-1][-1]

if __name__ == '__main__':
    ## Test cell

    # Run this cell to see how your function is working
    test_A1 = "WHOWEEKLY"
    test_B1 = "HOWONLY"

    lcs_val1 = lcs(test_A1, test_B1)

    test_A2 = "CATSINSPACETWO"
    test_B2 = "DOGSPACEWHO"
    
    lcs_val2 = lcs(test_A2, test_B2)

    print('LCS val 1 = ', lcs_val1)
    assert lcs_val1==5, "Incorrect LCS value."
    print('LCS val 2 = ', lcs_val2)
    assert lcs_val2==7, "Incorrect LCS value."
    print('Tests passed!')
