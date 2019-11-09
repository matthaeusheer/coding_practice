from typing import List, Dict, Type, Optional


def exc_16_2_word_frequencies(book: List[str]) -> Dict[str, int]:
    """Design a method to find the frequency of occurrences of any given word in a
    book. What if we were running this algorithm multiple times?
    Note: In the book this question is interpreted differently, such that the function takes in a word argument
          and the frequency of the word in the book is returned rather then doing it for all words.
    """
    lookup = {}
    for word in book:
        word = word.lower()
        if word not in lookup:
            lookup[word] = 1
        else:
            lookup[word] += 1
    return lookup

#########################
#                       #
#   Exercise 16.3       #
#                       #
#########################


class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y


class Line:
    def __init__(self, start: Point, end: Point) -> None:
        self.start = start
        self.end = end

    def y_at(self, x: float) -> float:
        return self.slope * x + self.y_intercept

    @property
    def slope(self):
        return (self.end.y - self.start.y) / (self.end.x - self.start.x)

    @property
    def y_intercept(self):
        return self.end.y - self.slope * self.end.x

    @staticmethod
    def intersection(first: 'Line', second: 'Line') -> Optional[float]:
        if Line.are_parallel(first, second):
            if Line.ranges_overlap(first, second):  # intersection for parallel lines with overlap
                return second.start.x  # calculate intersection
            else:  # no intersection
                return None
        else:  # for sure intersect
            return (second.y_intercept - first.y_intercept) / (first.slope - second.slope)

    @staticmethod
    def are_parallel(first: 'Line', second: 'Line') -> bool:
        return first.slope == second.slope

    @staticmethod
    def ranges_overlap(first: 'Line', second: 'Line') -> bool:
        """Assume ordered lines, i.e. first.start.x < second.start.x and start.x < end.x for both."""
        return value_in_range(second.start.x, first.start.x, first.end.x)


def value_in_range(val: float, start_range: float, end_range: float) -> Optional[bool]:
    return start_range <= val <= end_range


def exc_16_3_intersection(start1: Point, end1: Point, start2: Point, end2: Point) -> Optional[Point]:
    """Given two straight line segments (represented as a start point and an end point),
    compute the point of intersection, if any.
    Idea:   - Calculate both line equations
            - Calculate intersection point
            -
    """
    # Calculate line equations
    line1 = Line(start1, end1)
    line2 = Line(start2, end2)
    # Calculate intersection point
    x_intersect = Line.intersection(line1, line2)
    # Check if there is an intersection (different slopes or same slopes and line domain overlap
    if x_intersect:
        # Check if intersection point is within line ranges of both line equations
        if value_in_range(x_intersect, line1.start.x, line1.end.x) and value_in_range(x_intersect, line2.start.x, line2.end.x):
            y_coord = line1.y_at(x_intersect)
            return Point(x_intersect, y_coord)
    else:
        return None



