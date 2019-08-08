def Fibonacci(n):
    if n < 0:
        print ("Wrong number")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

def fib(n):
    """
    fib(1) => [0]
    fib(2) => [0, 1]
    fib(3) => [0, 1, 1]
    fib(4) => [0, 1, 1, 2]
    """
    result = [0]
    prev = 0
    curr = 1
    if n == 0:
        return result
    else:
        for i in range(n):       
            result.append(curr)
            curr, prev = curr + prev, curr
    return result


print(fib(100))

print(Fibonacci(9))
