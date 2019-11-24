
possible_paths = 0


def exc1_triple_step(stair_size: int) -> int:
    """A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3
    steps at a time. Implement a method to count how many possible ways the child can run up the
    stairs.

    Idea
    ----
        First consider a bottom-up approach. Standing at the bottom of the stairway, the child has
        three options, hop 1, 2 or 3. When it did the hops, it has again the possibility to hop 1, 2
        or 3. It can continue doing so until it reaches the top which is the base case. If it does so, we
        increase the counter of possible ways if it overshoots, we don't.
        Time:   O(3^n) since each node can have 3 children and the max depth of the tree is n for n hops of size 1
        Space:  O(logn) since this is the max height of the recursion stack
    """
    # Reset global variable if function is being called multiple times (e.g. multiple tests)
    global possible_paths
    possible_paths = 0

    def helper(hop_size, steps, total_steps):
        global possible_paths
        steps += hop_size
        if steps == total_steps:
            possible_paths += 1
            return
        elif steps > total_steps:
            return
        for s in [1, 2, 3]:
            helper(s, steps, total_steps)

    for step_size in [1, 2, 3]:
        helper(step_size, 0, stair_size)

    return possible_paths


def exc1_triple_step_no_global(stair_size: int) -> int:
    """Same as exc8_triple_step but without the need of a global variable and with memoization."""

    class Counter:
        def __init__(self):
            self.count = 0

    def recursive_helper(hop_size_, steps, total_steps, possibilities_counter_):
        steps += hop_size_
        if steps == total_steps:
            possibilities_counter_.count += 1
            return
        elif steps > total_steps:
            return
        for hop_size in [1, 2, 3]:
            recursive_helper(hop_size, steps, total_steps, possibilities_counter_)

    possibilities_counter = Counter()
    for step_size in [1, 2, 3]:
        recursive_helper(step_size, 0, stair_size, possibilities_counter)

    return possibilities_counter.count


def exc1_triple_step_top_down_memo(stair_size: int) -> int:
    """Now take a top-down approach which is trying to break down the big problem into smaller sub problems.
    Idea
    ----
        We know that before we jump on the last stair (n), we can be either on n-1 (and take a 1-stair hop) of be on
        n-2 (and take a double hop) or on n-3 and take a triple hop. These are
    """
    def count_ways(n, memo):
        if n < 0:
            return 0
        elif n == 0:  # Weird base case: 1 way for stair size 0 but it makes sense for higher stair sizes...
            return 1
        elif n in memo:
            return memo[n]
        else:
            memo[n] = count_ways(n - 1, memo) + \
                      count_ways(n - 2, memo) + \
                      count_ways(n - 3, memo)
            return memo[n]
    return count_ways(stair_size, {})


def exc2_robot_on_a_grid():
    pass