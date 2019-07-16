# https://github.com/minsuk-heo/problemsolving/blob/master/Craking%20the%20Coding%20Interview/1.5_compress_word.py

import unittest
"""
abbcccccccd -> a1b2c7d1
abc -> abc if the compression (a1b1c1) is longer than original, return original
"""
def compress_word(input):
    count = {}
    for s in input:
        if s in count:
            count[s] += 1
        else:
            count[s] = 1
    result = ''
    for k, v in count.items():
        result += k + str(v)

    return input if len(input) < len(result) else result    

class UnitTest(unittest.TestCase):
    def test(self):
        self.assertEqual("a1b2c7d1",compress_word("abbcccccccd"))
        self.assertEqual("a1b7c2d2", compress_word("abbbbbbbccdd"))
        self.assertEqual("abc", compress_word("abc"))
        self.assertEqual("aabcc", compress_word("aabcc"))

if __name__ == '__main__':
    unittest.main()