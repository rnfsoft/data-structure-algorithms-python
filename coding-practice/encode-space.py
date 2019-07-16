# https://github.com/minsuk-heo/problemsolving/blob/master/sort/BubbleSort.py
import unittest
"""
replace space with %20
ex)"hey how are you    "
return hey%20how%20are%20you
"""

def encode_space(input):
    return input.strip().replace(' ', '%20')


class UnitTest(unittest.TestCase):
    def test(self):
        self.assertTrue('hey%20how%20are%20you', 'hey how are you    ')

if __name__ == '__main__':
    unittest.main()


