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
    """
    Time:  O(2^n)  -> Since the recursive call tree has O(2^n) nodes representing calls and each call is O(1).
                      Since the call tree is actually not balanced (the right side is always smaller then left), the
                      actual runtime is O(1.6^n) but since BigO is an upper bound on runtime O(2^n) is still correct.
    Space: O(logn) -> Since at any moment at most max_depth(call_tree) stack frames are on the stack which is O(logn).
    """
    if n == 0 or n == 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_memoization(n: int, memo: dict = None) -> int:
    """
    Time:  O(n)    -> By caching results of each call results we have at most n calls to process.
    Space: O(n)    -> The memory requirement increases since we have the lookup table storing cached output.
    """
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
    result = last
    for idx in range(3, n + 1):
        result = last + second_last
        second_last = last
        last = result
    return result


def is_palindrome(num: int) -> bool:
    pass


