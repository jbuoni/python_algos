import unittest
import math

# Its pointless to do this, but we know the structure now
class Interval:
    def __init__(self):
        self.buy = None
        self.sell = None


def stock_prices(stocks):
    """
        The stock price problem involves buying and selling stocks where the stock is bought
        and sold. It has a complexity of O(n). It returns the index (day) when
        the stock should be bought to maximize profits.
        Performance is O(n) space complexity is O(n log n)
    """
    # If the array is empty, the maximum profit is zero.
    if len(stocks) == 0:
        return 0

    """
        Using recursion we get the left and right profit values
    """
    def stock_prices_recursion(arr, left, right):
        # There is no profit with 1 element
        if left == right:
            return_val = arr[left]
            return 0, return_val, return_val

        # Have to not use len of array because of the split
        mid = int(math.ceil(left + (right - left) / 2))

        # Get profits for both sides of the array recursively
        (leftProfit, leftMin, leftMax) = stock_prices_recursion(arr, left, mid)
        (rightProfit, rightMin, rightMax) = stock_prices_recursion(arr, mid + 1, right)

        # Covers if the best profit is on the left, right, or min is on left max is on right
        max_profit = max(leftProfit, rightProfit, rightMax - leftMin)

        return max_profit, min(leftMin, rightMin), max(leftMax, rightMax)

    profit, _, _ = stock_prices_recursion(stocks, 0, len(stocks) - 1)
    return profit


def stock_prices_dp(stocks):
    """
        Let profit = 0.
        Let min = arr[0]
        For k = 1 to length(arr):
           If arr[k] < min,  min = arr[k]
           If profit < arr[k] - min, set profit = arr[k] - min

    :param stocks:
    :return:
    """
    # If the array is empty, the maximum profit is zero.
    if len(stocks) == 0:
        return 0

    profit = 0
    cheapest = stocks[0]

    for n in range(1, len(stocks)):
        cheapest = min(cheapest, stocks[n])
        profit = max(profit, stocks[n] - cheapest)

    return profit


class Test(unittest.TestCase):
    def test_stock_prices(self):
        stocks = [2, 3, 10, 6, 4, 8, 1]
        self.assertEqual(stock_prices(stocks), 8)
        stocks = [7, 9, 5, 6, 3, 2]
        self.assertEqual(stock_prices(stocks), 2)

    def test_stock_prices_dp(self):
        stocks = [2, 3, 10, 6, 4, 8, 1]
        self.assertEqual(stock_prices_dp(stocks), 8)
        stocks = [7, 9, 5, 6, 3, 2]
        self.assertEqual(stock_prices_dp(stocks), 2)

