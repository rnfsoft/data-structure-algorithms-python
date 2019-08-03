import unittest

def quick_sort(input):
    if len(input) < 2:
        return input
    
    pivot = input[0]
    smaller = [i for i in input[1:] if i <= pivot]
    larger = [i for i in input[1:] if i > pivot]

    input = quick_sort(smaller) + [pivot] + quick_sort(larger)

    return input

class UnitTest(unittest.TestCase):
    def test(self):
        self.assertEqual([1,2,3,4,5,6,7,8,9,10], quick_sort([10,9,8,7,6,5,4,3,2,1]))


if __name__ == '__main__':
    unittest.main()