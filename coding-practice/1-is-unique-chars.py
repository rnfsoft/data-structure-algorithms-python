import unittest

# def is_unique_chars(str):
#     if len(str)> 256:
#         return False
    
#     hash = [False] *256 # [False, False, .....]

#     for s in str:
#         if (hash[ord(s)]) is True: # ord('a') : 97, ord('b'): 98
#             return False
#         else:
#             hash[ord(s)] = True
#     return True

def is_unique_chars(str):
    chars = {}
    for s in str:
        if s in chars:
            chars[s] += 1
        else:
            chars[s] = 1
    return all(v < 2 for v in chars.values())

class UniTest(unittest.TestCase):
    def test(self):
        input_unique = "abcde"
        input_not_unique = "abcdea"
        self.assertTrue(is_unique_chars(input_unique))
        self.assertFalse(is_unique_chars(input_not_unique))

if __name__ == '__main__':
    unittest.main()