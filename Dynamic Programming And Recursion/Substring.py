"""
    Dynamic Programming algorithms involving substrings
"""
import unittest


def longest_common_substring(x, y):
    """
        Input: StringsArrays x, y
        Output: Length of the longest common substring in x, y
        Subproblem: For 0<=i<=n 0<=j<=m let T(i, j) = length of the longest palindrome sub sequence in x=x1,x2,...xi
            and y=y1,y2,...yj which includes xi, yj

        time complexity is O(x * y) as is space complexity
    :param x
    :param y
    :return:
    """
    i_len = range(len(x) + 1)
    j_len = range(len(y) + 1)

    # Int table of all 0s
    t = [[0 for i in i_len] for j in j_len]
    imax = 0
    jmax = 0

    # Check each character at start and end of string,
    # If there is a match then increment the count
    for i in i_len:
        for j in range(i, len(j_len)):
            if i == 0 or j == 0:
                t[i][j] = 0
            elif x[i - 1] == y[j - 1]:
                new_cell = t[i - 1][j - 1] + 1
                t[i][j] = new_cell
                if new_cell > t[imax][jmax]:
                    imax = i
                    jmax = j
            else:
                t[i][j] = 0

    return t[imax][jmax]


def longest_palindrome_subsequence(x):
    """
        Input: String s
        Output: Length of the longest palindrome subsequence in s
        Subproblem: For 0<=i<=n let T(i, j) = length of the longest palindrome
            sub sequence in s = s1,s2,...si which includes si

        time complexity is O(x^2) as is space complexity
    :param x:
    :return:
    """
    range_x = range(len(x))
    t = [[0 for j in range_x] for i in range_x]

    imax = 0
    jmax = 0

    # Same character is always a 1
    for j in range_x:
        t[j][j] = 1

    for i in range_x:
        for j in range(i, len(x) - 1):
            if x[i] == x[j]:
                # If we are one character ahead just add 1
                if j == (i + 1):
                    t[i][j] = 2
                else:
                    # There is a character in between, so add 2
                    # Which we are at most
                    t[i][j] = 2 + t[i + 1][j - 1]
            else:
                t[i][j] = t[i + 1][j - 1]

            if t[imax][jmax] < t[i][j]:
                imax = i
                jmax = j

    # This is unnecessary but its how I learned at Tech
    return t[imax][jmax]


def longest_palindrome_substring(x):
    """
        Input: String s
        Output: Length of the longest palindrome substring in s
        Subproblem: For 0<=j<=n 0<=i<=j let T(i, j) = length of the longest palindrome sub
            sequence in s = s1,s2,...si which includes si, sj

        time complexity is O(x^2) as is space complexity
    :param x:
    :return:
    """

    n = len(x)
    # Init table
    t = [[0 for i in range(n)] for l in range(n)]

    # Mark each table item as true. Store the length separately, but use the previous value
    # or False to determine if we should keep going. This makes it easier they trying to add and
    # subtract sub arrays
    max_len = 1

    # Set the same letter to True
    for j in range(n - 1):
        if x[j] == x[j + 1]:
            t[j][j + 1] = True
            max_len = 2

    # In this case, substring has to be at min size 3 (to beat max)
    k = 3  # Length of substring
    while k < n:
        i = 0
        while i < n - k + 1:
            # Get the ending index of
            # substring from starting
            # index i and length k
            j = k + i - 1
            # Check to see if the previous value is true. If so, set to True
            if t[i + 1][j - 1] and x[i] == x[j]:
                t[i][j] = True
                # If we are already at a higher K then set max len
                max_len = k if max_len < k else max_len
            i += 1
        k += 1  # Increment substring

    return max_len


class Tests(unittest.TestCase):
    def test_longest_common_substring(self):
        X = 'OldSite:GeeksforGeeks.org'
        Y = 'NewSite:GeeksQuiz.com'

        lcs = longest_common_substring(X, Y)
        self.assertTrue(10, lcs)

    def test_longest_palindrome_subsequence(self):
        X = " AABCDEBAZ"
        lps = longest_palindrome_subsequence(X)
        self.assertTrue(5, lps)

    def test_longest_palindrome_substring(self):
        X = " forgeeksskeegfor"
        lps = longest_palindrome_substring(X)
        self.assertTrue(10, lps)
