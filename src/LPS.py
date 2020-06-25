"""
Longest Palindromic Subsequence
Dynamic Programming

In general, a palindrome is a string that reads the same backwards as forwards, 
e.g., MADAM. In the last notebook, we saw that in a given string, a subsequence 
is an ordered set of characters that need not necessarily be a contiguous 
substring, e.g., ABC is a subsequence in AXBYC with length = 3.

The Longest Palindromic Subsequence (LPS) is the most lengthy sequence of 
characters that is a palindrome. In this notebook, you'll be tasked with 
finding the length of the LPS in a given string of characters.

Examples:

    With an input string, MAXDYAM, the LPS is MADAM, which has length = 5
    With an input string, BxAoNxAoNxA, the LPS is ANANA, which has length = 5
    With an input string, BANANO, the LPS is NAN, which has length = 3
    With an input string, ABBDBCACB, the LPS is BCACB, which has length = 5
"""
def lps(input_string):
    # Return the LPS length for the given input string
    n = len(input_string)
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(0, n):
        matrix[i][i] = 1
    
    # Traverse the word for all the different substring lenghts
    # The start index corresponds to the row in the matrix, while the end
    # index corresponds to the column
    # So, we're going from the matrix diagonal to the upper rightmost cell
    for substr_len in range(2, n + 1):
        for start in range(n - substr_len + 1):
            end = start + substr_len - 1
            # match between the start and end of the substring
            if input_string[start] == input_string[end]:
                # fill this cell with the value to the bottom-left plus two
                matrix[start][end] = matrix[start + 1][end - 1] + 2
            else:
                # take the max value from either the cell directly to the left or bottom
                matrix[start][end] = max(matrix[start][end - 1], matrix[start + 1][end])

    # return the value at the top right corner of the matrix
    return matrix[0][-1]

def test_function(test_case):
    string = test_case[0]
    solution = test_case[1]
    output = lps(string)
    print(output)
    if output == solution:
        print("Pass")
    else:
        print("Fail")

if __name__ == '__main__':
    # Test case 1
    string = 'BxAoNxAoNxA'
    solution = 5
    test_case = [string, solution]
    test_function(test_case)

    # Test case 2
    string = 'BANANO'
    solution = 3
    test_case = [string, solution]
    test_function(test_case)

    # Test case 3
    string = "TACOCAT"
    solution = 7
    test_case = [string, solution]
    test_function(test_case)
