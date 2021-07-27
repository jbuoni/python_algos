"""
    Input: Change denominations x=x1,x2,...xn, value v
    Output: If change can be made for value v using coins x
    Subproblem (repeat): For 0<=i<=n 0<=b<=v let T(i, b) = true if change can be made for value b using coins x=x1,x2,..xi which includes xi.
    Subproblem (no repeat): For 0<=i<=n 0<=b<=v let T(i, b) = true if change can be made for value b using coins x=x1,x2,..xi which includes xi.
                            Each coin can only be used once.
"""

import unittest


def coin_change(coins, value):
    """
        More or less make a 2D table that will contain all possible iterations of the
        value and the change needed to make such values

        Time complexity: O(cb)
        Space complexity: O(cb)

        Note: This will determine if we have the coins to make some sort of change, and not exact change
    :param coins:
    :param value:
    :return:
    """
    t = [[0 for x in range(len(coins))] for y in range(value + 1)]

    for i in range(len(coins)):
        t[0][i] = 1  # Init

    # Fill the rest of the table from the bottom up
    for i in range(1, value + 1):
        for j in range(len(coins)):
            # The number of possible variations of change up to this point
            k = t[i - coins[j]][j] if i - coins[j] >= 0 else 0
            b = t[i][j - 1] if j >= 1 else 0

            t[i][j] = k + b

    return t[value][len(coins) - 1]


def coin_change_no_repeat(coins, value):
    """
        More or less make a 2D table that will contain all possible iterations of the
        value and the change needed to make such values. Same as above but no repeating

        Time complexity: O(cb)
        Space complexity: O(cb)

        Note: This will determine if we have the coins to make some sort of change, and not exact change
    :param coins:
    :param value:
    :return: True if you can make change and false if you cannot
    """
    t = [[0 for x in range(value + 1)] for y in range(len(coins))]

    for i in range(len(coins)):
        t[i][0] = 1

    for b in range(value + 1):
        if b >= 1:
            t[0][b] = 0

    for i in range(len(coins)):
        for b in range(value + 1):
            if coins[i] <= b:
                t[i][b] = t[i - 1][b - coins[i]] + 1
            else:
                t[i][b] = t[i - 1][b]
    return t[len(coins) - 1][value]


def can_make_change(coins, v):
    """
        Same as the ones above but return true or false
    :param coins:
    :param v:
    :return:
    """
    t = [[False for x in range(v + 1)] for y in range(len(coins))]
    t[0][0] = True

    for i in range(len(coins)):
        t[i][0] = True

    for b in range(v + 1):
        if b >= 1:
            t[0][b] = False

    for i in range(len(coins)):
        for b in range(v + 1):
            if coins[i] <= b:
                t[i][b] = t[i][b - coins[i]] or t[i-1][b - coins[i]]
            else:
                t[i][b] = t[i-1][b]
    return t[len(coins) - 1][v - 1]


def can_make_change_no_repeat(coins, v):
    """
        Same as the ones above but return true or false
    :param coins:
    :param v:
    :return:
    """
    t = [[False for x in range(v + 1)] for y in range(len(coins))]
    t[0][0] = True

    for i in range(len(coins)):
        t[i][0] = True

    for b in range(v + 1):
        if b >= 1:
            t[0][b] = False

    for i in range(len(coins)):
        for b in range(v + 1):
            if coins[i] <= b:
                t[i][b] = t[i-1][b - coins[i]]
            else:
                t[i][b] = t[i-1][b]
    return t[len(coins) - 1][v]


def least_coins(coins, value):
    added_coins = []
    i = len(coins) - 1

    while i >= 0:
        while coins[i] <= value:
            value -= coins[i]
            added_coins.append(coins[i])

        i -= 1

    return added_coins


class Test(unittest.TestCase):
    coins = [1, 2, 3]
    coins1 = [5, 10, 25, 50]
    coins2 = [1, 5, 10, 25, 50]

    def test_coin_change(self):
        self.assertEqual(coin_change(self.coins, 4), 4)
        self.assertEqual(coin_change(self.coins1, 15), 2)
        self.assertEqual(coin_change(self.coins2, 30), 18)

    def test_coin_change_no_repeat(self):
        self.assertEqual(coin_change_no_repeat(self.coins, 4), 3)
        self.assertEqual(coin_change_no_repeat(self.coins1, 15), 3)
        self.assertEqual(coin_change_no_repeat(self.coins2, 30), 3)

    def test_can_make_change(self):
        self.assertEqual(can_make_change_no_repeat(self.coins, 4), True)
        self.assertEqual(can_make_change_no_repeat(self.coins1, 1), False)
        self.assertEqual(can_make_change_no_repeat(self.coins2, 30), True)

    def test_can_make_change_no_repeat(self):
        self.assertEqual(can_make_change_no_repeat(self.coins, 4), True)
        self.assertEqual(can_make_change_no_repeat(self.coins1, 10000), False)
        self.assertEqual(can_make_change_no_repeat(self.coins2, 30), True)

    def test_least_coins(self):
        coins = [1, 2, 5, 10, 20, 50, 100, 500, 1000]
        self.assertEqual(least_coins(coins, 93), [50, 20, 20, 2, 1])
        self.assertEqual(least_coins(coins, 53), [50, 2, 1])
