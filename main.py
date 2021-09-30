#calculator.py


def sum(m, n):
    if n > 0:
        while n != 0:
            m = m+1
            n = n-1
    elif n < 0:
        while n != 0:
            m = m - 1
            n = n + 1
    return m


def divide(m, n):
    result = 0
    if n > m or n == 0:
        return 0
    if n > 0:
        while m >= n:
            m = m-n
    if n < 0:
        while m > n:
            m = m + n
            result += 1
    return result
