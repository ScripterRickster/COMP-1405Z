def sum_divisors(N):
    divisor = 1
    total = 0

    while divisor <= N:
        if N % divisor == 0:
            total += divisor
        divisor += 1

    return total
