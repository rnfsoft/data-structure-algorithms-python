import unittest

def merge_sort(input):
    if len(input) > 1:
        mid = len(input) //2
        left = input[:mid]
        right = input[mid:]

        left = merge_sort(left)
        right = merge_sort(right)

        lidx, ridx, idx = 0, 0, 0

        while lidx < len(left) and ridx < len(right):
            if left[lidx] < right[ridx]:
                input[idx] = left[lidx]
                idx += 1
                lidx += 1
            else:
                input[idx] = right[ridx]
                idx += 1
                ridx +=1
        while lidx < len(left):
            input[idx] = left[lidx]
            idx +=1
            lidx +=1
        while ridx < len(right):
            input[idx] = right[ridx]
            idx +=1
            ridx +=1
    return input

class UnitTest(unittest.TestCase):
    def test(self):
        self.assertEqual([1,2,3,4,5,6,7,8,9,10], merge_sort([10,9,8,7,6,5,4,3,2,1]))


if __name__ == '__main__':
    unittest.main()