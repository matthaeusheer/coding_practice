def factorial(n: int) -> int:
    if n == 1:
        return 1
    return n * factorial(n - 1)


def factorial_iterative(n: int) -> int:
    result = 1
    idx = n
    while idx > 1:
        result *= idx
        idx -= 1
    return result


def fibonacci(n: int) -> int:
    if n == 0 or n == 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_memoization(n: int, memo: dict = None) -> int:
    memo = memo if memo else {0: 1, 1: 1}  # Since we really, really have to avoid mutable default args :-)
    if n == 0 or n == 1:
        return n
    if n in memo:
        return memo[n]
    result = fibonacci_memoization(n - 1, memo) + fibonacci_memoization(n - 2, memo)
    memo[n] = result
    return result


def fibonacci_iterative(n: int) -> int:
    if n == 0 or n == 1:
        return n
    second_last = 1
    last = 1
    result = None
    for idx in range(3, n + 1):
        result = last + second_last
        second_last = last
        last = result
    return result


def is_palindrome(num: int) -> bool:
    pass


