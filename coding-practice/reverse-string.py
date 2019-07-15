import unittest

# def reverse_string(input):
#     return input[::-1]

def reverse_string(input):
    stack = []
    for s in input:
        stack.append(s)

    result = ''
    while stack:
        result += stack.pop()

    return result




class UnitTest(unittest.TestCase):
    def test(self):
        input = 'abcde'
        self.assertEqual('edcba', reverse_string(input))


if __name__ == '__main__':
    unittest.main()