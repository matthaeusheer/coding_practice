"""
Solving coding exercises from "Cracking the Coding Interview", Chapter 1 - Arrays and Strings.

Author: Matthaeus Heer
"""


def exc1_is_unique_1(input_str: str) -> bool:
    """Implement an algorithm to determine if a string has all unique characters.
    What if you cannot use additional data structures?
    Hints:
    - Try a hash table
    - Could a bit vector be useful?
    - Can you solve it in O(n logn)? What might a solution like that look like?
    """
    # Idea: Go through characters in input string and put them into a dict (hast table).
    # Then, when at some point a character comes up which is already in the dict as a key, we know
    # the string is not unique -> correct solution!
    # Assume ASCII string (ask interviewer whether ASCII or Unicode).
    # Time complexity:
    #   O(n) [need to go through every character]
    #   O(1) [if we assume ASCII and we will never loop through more then 128 chars or 256 for extended ASCII]
    # Space complexity:
    #   O(1) [if possible character set is fixed in size]
    #   O(min(len(input_str), c) if this assumption is not take, c = size char set]
    #
    # Version bit vector:
    #   Can reduce space by factor of 8, not done here.
    # Version no additional data structures:
    #   Compare every entry with all other entries O(n²) time and O(1) space
    #   We could sort beforehand O(n logn) time and O(...) space (depends on sorting algo) and then check for
    #   neighboring identical characters, this part is O(1) space.
    letters = {}
    for character in input_str:  # O(n) loop
        if character in letters.keys():  # O(1) lookup amortized
            return False
        letters[character] = True
    return True


def exc2_check_permutation(first: str, second: str) -> bool:
    """Given two strings, write a method to decide if one is a permutation of the other.
    Hints:
    - Describe what it means for two strings to be permutations of each other. Now, look at
      that definition you provided. Can you check the strings against that definition?
    - There is one solution that is 0( N log N) time. Another solution uses some space, but
      is O(N) time.
    - Hash table?
    - Two strings that are permutations should have the same characters, but in different
      orders. Can you make the orders the same?
    """
    # Questions to clarify: Is permutation case-sensitive? Is the problem whitespace-sensitive?

    # A permutation ofa string is a re-arrangement of the characters of the string.
    # If it is possible to re-arrange letters in one string (permutation) such that they equal
    # a second string, the two strings are permutations of each other.

    # Idea 1: Sort both strings and compare if they are equal.
    #   Sorting takes twice 2*O(n log n), comparing each entry O(n), so total O(n logn) time
    #   Space complexity depends on sorting algorithm O(1) heap sort, O(logn) quicksort
    return sorted(first) == sorted(second)


def exc2_check_permutation_2(first: str, second: str) -> bool:
    # Idea 2:
    #   Check if two strings have identical character counts, because if they do, one can re-arrange
    #   one of them to equal the second one.
    #   Time: O(n), n length of word since we have to go through whole word
    #   Space: O(n), have to store a count value for each character in words
    if len(first) != len(second):
        return False

    char_cts_first = {}
    char_cts_second = {}

    def update_ct(cts_dict, char):
        # works since we pass by name (object itself which is mutable since we pass a dict)
        if char in cts_dict:
            cts_dict[char] += 1
        else:
            cts_dict[char] = 1

    for char_first, char_second in zip(first, second):
        update_ct(char_cts_first, char_first)
        update_ct(char_cts_second, char_second)

    if char_cts_first == char_cts_second:  # check if both dicts which represent word counts are the same
        return True
    else:
        return False


def exc3_urlify(string: str, true_length: int) -> str:
    """Write a method to replace all spaces in a string with '%20'. You may assume that the string
    has sufficient space at the end to hold the additional characters, and that you are given the "true"
    length of the string.
    EXAMPLE
        Input: "Mr John Smith     ", 13
        Output: "Mr%20John%20Smith"
    Hints:
    - It's often easiest to modify strings by going from the end of the string to the beginning.
    - You might find you need to know the number of spaces. Can you just count them?
    """
    # Idea 1:
    #   Loop once through the string and record the starting and endpoints of whitespace sections.
    #   Then go from end to front of string and change the sections, that way dealing with
    #   indices will not fail after a modification.
    string = string.strip()
    string = string.replace(' ', '%20')
    return string
