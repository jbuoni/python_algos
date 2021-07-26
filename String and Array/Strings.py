from copy import deepcopy
import unittest


def programmer_subsequence(s):
    """
        Return the number of instances 'programmer' is in a string
        the word does not have to be continuous or in order,
        'programmerprogrammer' returns 0, as it cannot be one after the 
        other
    """

    # Base case. Remove all instances where programmer repeats
    s = s.replace('programmerprogrammer', '')

    template = {
        'p': 0,
        'r': 0,
        'o': 0,
        'g': 0,
        'a': 0,
        'm': 0,
        'e': 0
    }

    matches = [] # Tuple of start and ends
    i= 0
    P_LENGTH = 9 # Length of the word 'programmer'

    k = P_LENGTH  # Temp
    while i + k < len(s):
        # Make substring
        sub_s = s[i:i + k]

        copy_t = deepcopy(template)
        # Check to see if all chars are contained within string
        for j in range(len(sub_s)):
            if sub_s[j] in ['r', 'm']:
                copy_t[sub_s[j]] += 1 if copy_t[sub_s[j]] < 2 else copy_t[sub_s[j]]
            elif sub_s[j] in copy_t:
                copy_t[sub_s[j]] = 1 

        # If we have all values, then inceremnt count and check the next P_LENGTH string
        if sum(copy_t.values()) == P_LENGTH:
            matches.append((i, k))
            i += P_LENGTH
            j = P_LENGTH # Reset J
        else:
            k += 1

    return len(matches)

class Test(unittest.TestCase):
    def test_programmer_subsequence(self):
        s = 'pirioigiriaimimieir'
        self.assertEqual(programmer_subsequence(s), 1)
        s = 'pirioigiriaimimieirpirioigiriaimimieir'
        self.assertEqual(programmer_subsequence(s), 2)
        s = 'pioirigirimiaimieirpirioigiriaimimieir'
        self.assertEqual(programmer_subsequence(s), 2)
        s = 'programmerprogrammer'
        self.assertEqual(programmer_subsequence(s), 0)
