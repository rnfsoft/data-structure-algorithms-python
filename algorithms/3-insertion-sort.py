# https://github.com/minsuk-heo/problemsolving/blob/master/sort/InsertionSort.py

import unittest

def insertion_sort(input):
    for i, value in enumerate(input):
        while i > 0 and input[i-1] > value:
            input[i-1], input[i] = input[i], input[i-1]
            i -= 1
    return input

class UnitTest(unittest.TestCase):
    def test(self):
        self.assertEqual([1,2,3,4,5,6], insertion_sort([4,6,1,3,5,2]))
        self.assertEqual([1, 2, 3, 4, 5, 6], insertion_sort([6, 4, 3, 1, 2, 5]))
        self.assertEqual([1, 2, 3, 4, 5, 6], insertion_sort([6, 5, 4, 3, 2, 1]))


if __name__ == '__main__':
    unittest.main()