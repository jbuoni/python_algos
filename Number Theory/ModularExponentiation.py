"""
    Modular Exponentiation for large numbers


    Input: The first line of input consists number of the test cases.
    The following T lines consist of 3 numbers each separated by a space and in the following order:
    A B C
    'A' being the base number, 'B' the exponent (power to the base number) and 'C' the modular.
    Output: In each separate line print the modular exponent of the given numbers in the test case.

    Time complexity: O(log y)
"""

import unittest


def modular_exponentiation(a, b, c):
    result = 1

    a = a % c  # If a is more than or equal to p. Prevents overflows

    while b > 0:
        # If b is odd multiply
        # Use bitwise functions here. Figure out about that
        if (b & 1) == 1:
            result = (result * a) % c

        # Bitwise b/2
        b = b >> 1
        a = (a * a) % c  # Prevent overflow

    return result


class Test(unittest.TestCase):

    def test_modular_exponentiation(self):
        self.assertEqual(modular_exponentiation(2, 5, 13), 6)
        self.assertEqual(modular_exponentiation(2, 3, 5), 3)
        self.assertEqual(modular_exponentiation(3, 2, 4), 1)
        self.assertEqual(modular_exponentiation(10, 9, 6), 4)
        self.assertEqual(modular_exponentiation(450, 768, 517), 34)
