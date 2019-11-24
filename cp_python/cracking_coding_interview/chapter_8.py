import copy
from typing import List, Optional


global_possible_paths = 0


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
    global global_possible_paths
    global_possible_paths = 0

    def helper(hop_size, steps, total_steps):
        global global_possible_paths
        steps += hop_size
        if steps == total_steps:
            global_possible_paths += 1
            return
        elif steps > total_steps:
            return
        for s in [1, 2, 3]:
            helper(s, steps, total_steps)

    for step_size in [1, 2, 3]:
        helper(step_size, 0, stair_size)

    return global_possible_paths


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


class GridPoint:
    def __init__(self, row, col):
        self.row, self.col = row, col

    def __eq__(self, other):
        return self.row == other.row and self.col == other.col

    def __repr__(self):
        return f'GridPoint: (row: {self.row}, col: {self.col})'

    def right_neighbour(self):
        return GridPoint(row=self.row, col=self.col + 1)

    def lower_neighbour(self):
        return GridPoint(row=self.row + 1, col=self.col)


class Grid:
    def __init__(self, rows, cols) -> None:
        self.grid = [cols * [True] for _ in range(rows)]
        self.rows = rows
        self.cols = cols

    def __repr__(self):
        rep = f'Grid: ({len(self.grid)} rows, {len(self.grid[0])} cols)\n'
        for row in self.grid:
            row_str = ''
            for entry in row:
                row_str += f'{"o" if entry else "x":>5}'
            rep += (row_str + '\n')
        return rep

    def occupy_cell(self, row: int, col: int) -> None:
        self.grid[row][col] = False

    def is_occupied(self, point: GridPoint) -> bool:
        if point.row >= self.rows or point.col >= self.cols:
            return True
        return not self.grid[point.row][point.col]

    def get_lower_right(self) -> GridPoint:
        return GridPoint(row=self.rows - 1, col=self.cols - 1)

    @staticmethod
    def get_upper_left() -> GridPoint:
        return GridPoint(0, 0)


def exc2_robot_on_a_grid(grid: Grid) -> Optional[List[GridPoint]]:
    """Imagine a robot sitting on the upper left corner of grid with r rows and c columns.
    The robot can only move in two directions, right and down, but certain cells are "off limits" such that
    the robot cannot step on them. Design an algorithm to find a path for the robot from the top left to
    the bottom right."""
    robo_path = []  # the list of points for a path we find

    def find_path(grid: Grid, point: GridPoint, path) -> bool:
        if point == grid.get_lower_right():
            print('\tHey, I arrived at the target!')
            return True
        if not grid.is_occupied(point.right_neighbour()):
            print(f'Going to {point.right_neighbour()}')
            path.append(point)
            if find_path(grid, point.right_neighbour(), path):
                return True
        if not grid.is_occupied(point.lower_neighbour()):
            print(f'Going to {point.lower_neighbour()}')
            path.append(point)
            if find_path(grid, point.lower_neighbour(), path):
                return True
        print(f'\tI am stuck at {point}')
        return False

    if find_path(grid, GridPoint(0, 0), robo_path):
        return robo_path
    else:
        return None
