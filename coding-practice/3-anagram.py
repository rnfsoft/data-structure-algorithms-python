import unittest


# def anagram(str1, str2):
#     return True if sorted([s for s in str1.strip()]) == sorted([s for s in str2.strip()]) else False

def anagram(str1, str2):
    return sorted(str1) == sorted(str2)

class UnitTest(unittest.TestCase):
    def test(self):
        self.assertTrue(anagram('listen', 'silent'))
        self.assertFalse(anagram('abc', 'def'))

if __name__ == '__main__':
    unittest.main()