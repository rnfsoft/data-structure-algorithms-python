# https://github.com/minsuk-heo/problemsolving/blob/master/sort/SelectionSort.py

import unittest

def selectionSort(input):
    for i in range(len(input) -1):
        min_idx = i
        j = i + 1
        
        while j < len(input):
            if input[j] < input[min_idx]:
                min_idx = j
            j += 1
        
        if min_idx is not i:
            input[min_idx], input[i]= input[i], input[min_idx]
    return input




class UnitTest(unittest.TestCase):
    def test(self):
        self.assertEqual([1,2,3,4,5,6], selectionSort([4,6,1,3,5,2]))
        self.assertEqual([1, 2, 3, 4, 5, 6], selectionSort([6, 4, 3, 1, 2, 5]))
        self.assertEqual([1, 2, 3, 4, 5, 6], selectionSort([6, 5, 4, 3, 2, 1]))

if __name__ == '__main__':
   unittest.main()