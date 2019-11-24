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
    """Basically this is a dynamic programming solution (see below)."""
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


def fibonacci_dyn_progr(n: int) -> int:
    """Bottom-up dynamic programming approach. Rather then starting from the top problem and
    recursing down until we reach the base cases, we start from the actual base cases and
    use those to build up the solution gradually.
    Time:   O(n) since we have to do at most n calls, all others are cached
    Space:  O(n) space needed for the memo
    """
    if n == 0 or n == 1:
        return n
    memo = {0: 0, 1: 1}
    for idx in range(2, n):
        memo[idx] = memo[idx - 1] + memo[idx - 2]
    return memo[n - 1] + memo[n - 2]


def fibonacci_dyn_progr_2(n: int) -> int:
    """In fibonacci_dyn_progr we don't actually need to store the whole memo since we only ever
    use the last two values in it. Therefor we can reduce the space requirements from O(n) to O(1).
    Time:   O(n) since we simply traverse through the n levels from bottom up
    Space:  O(1) we need no more memo since the two last values are enough
    """
    if n == 0 or n == 1:
        return n
    last = 1
    second_last = 0
    for idx in range(2, n):
        res = last + second_last
        second_last = last
        last = res
    return last + second_last


def is_palindrome(num: int) -> bool:
    pass


def power_recursive(base: int, exp: int) -> int:
    """Write a function that returns base^exp without the use of **-operator.
    Without the even-exponent-optimization the runtime would be O(exp) just like the iterative approach since
    in that case they are basically the same. Note that this recursive version uses O(exp) space as well while the
    iterative version is O(1) space. However, with the even-exponent optimization we can actually bring down the
    number of multiplications needed as well as the space needed."""
    if exp == 0:
        return 1
    if exp % 2 == 0:
        temp = power_recursive(base, exp // 2)
        return temp * temp
    return base * power_recursive(base, exp - 1)


def power_iterative(base: int, exp: int) -> int:
    """Iterative version. Note that we need exp multiplications, hence runtime is O(exp), while space is O(1)."""
    result = 1
    for _ in range(exp):
        result *= base
    return result
