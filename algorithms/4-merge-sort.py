import unittest

def merge_sort(input):
    if len(input) > 1:
        mid = len(input) // 2
        l = input[:mid]
        r = input[mid:]

        merge_sort(l)
        merge_sort(r)

        i = j = k = 0

        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                input[k] = l[i]
                i += 1
                k += 1
            else:
                input[k] = r[j]
                j += 1
                k += 1

        while i < len(l): 
            input[k] = l[i] 
            i+=1
            k+=1
          
        while j < len(r): 
            input[k] = r[j] 
            j+=1
            k+=1
        return input
            
class UnitTest(unittest.TestCase):
    def test(self):
        self.assertEqual([1,2,3,4,5,6,7,8,9,10], merge_sort([10,9,8,7,6,5,4,3,2,1]))

if __name__ == '__main__':
    unittest.main()