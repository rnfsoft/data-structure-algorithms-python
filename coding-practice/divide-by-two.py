from stack import Stack

def divide_by_two(num):
    stack = Stack()

    while num > 0:
        stack.push(num%2)
        num = num // 2
    result = ''
    while not stack.is_empty():
        result += str(stack.pop())
    return result

print(divide_by_two(1024))