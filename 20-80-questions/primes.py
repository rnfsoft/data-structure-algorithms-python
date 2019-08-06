def primes(number):
    primes = []
    for num in range(number+1):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                primes.append(num)
    return primes

print(primes(1000000))