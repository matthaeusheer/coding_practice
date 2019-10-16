"""
Solving coding exercises from "Cracking the Coding Interview", Chapter 1 - Arrays and Strings.

Author: Matthaeus Heer
"""
from typing import List


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


def exc4_palindrome_permutation(input_string: str) -> bool:
    """Given a string, write a function to check if it is a permutation of a palin­
    drome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation
    is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
    Example:
        Input: Tact Coa
        Output: True: ("taco cat", "atco cta", ...)
    Hints:
    - You do not have to-and should not-generate all permutations. This would be very inefficient.
    - What characteristics would a string that is a permutation of a palindrome have?
        It would have equal number of each character except maybe one which could be not equal
    - Have you tried a hash table? You should be able to get this down to 0( N) time.
    - Can you reduce the space usage by using a bit vector?
    """
    # Idea: Hash table with counters for individual characters, fill it up, then go through it and check
    # whether the contraints are valid.
    # Complexity:
    #   Time: O(n) going through whole input, then O(n) to check, hash table lookup is O(1), so 2*O(n) which is O(n)
    #         Note: Not optimizable since every algorithm has to check every character in the input string
    #   Space: O(1) if input size is fixes, else O(len(input_string))

    # Pre-processing: Cut away whitespaces and lower since we are not case sensitive (needs to be asked!)
    input_string = input_string.replace(' ', '').lower()

    # For every char, count the number of times it appears
    char_counter = {}
    for char in input_string:
        if char not in char_counter.keys():
            char_counter[char] = 1
        else:
            char_counter[char] += 1

    def is_even(number):
        return number % 2 == 0

    n_uneven_chars = 0
    for count in char_counter.values():
        if not is_even(count):
            n_uneven_chars += 1
        if n_uneven_chars > 1:
            print(f'{input_string} is not a permutation of a palindrome!')
            return False
    print(f'{input_string} is a permutation of a palindrome!')
    return True


def exc5_one_away(str1: str, str2: str) -> bool:
    """There are three types of edits that can be performed on strings: insert a character,
    remove a character, or replace a character. Given two strings, write a function to check if they are
    one edit (or zero edits) away.
    Hints: #23, #97, #130
    - Start with the easy thing. Can you check each of the conditions separately?
    - What is the relationship between the "insert character" option and the "remove char­acter" option?
      Do these need to be two separate checks?
    - Can you do all three checks in a single pass?
    """
    # Complexity:
    #   Time: O(n), n = #elements in longer string
    #   Space: O(1)

    def check_replace(s1, s2):
        """Check if one can make s1 into s2 by replacing one character. If we have to modify more than one this is
        certainly not possible so we return False if we have more than 1 edits.
        Else, for 0 or 1 edits, we return True."""
        edit_found_already = False
        for char1, char2 in zip(s1, s2):
            if char1 != char2:
                if edit_found_already:
                    return False  # if we come here twice we need more than one edit
            edit_found_already = True
        return True

    def check_insert(s1, s2):
        """Check if we can make s1 to s2 by inserting one letter. Checking if one can make one string into another
        by removing a letter is the same as checking whether one can inserting one letter into the second to make it
        the first one, so inserting is the inverse of removal of one letter."""
        idx1 = 0
        idx2 = 0
        while idx1 < len(s1) and idx2 < len(s2):
            char1, char2 = s1[idx1], s2[idx2]
            if char1 != char2:
                if idx1 != idx2:
                    return False
                idx2 += 1  # we inserted a character in s2, so we advance here only to sync up to s1
            else:
                idx1 += 1
                idx2 += 1
        return True

    # Lengths of the strings determine which check should be implemented.
    if len(str2) == len(str1):
        return check_replace(str1, str2)
    elif len(str1) == len(str2) - 1:
        return check_insert(str1, str2)
    elif len(str1) == len(str2) + 1:
        return check_insert(str2, str1)  # inverse of insertion
    return False  # if they are not same length or one apart


def exc6_string_compression(input_str: str) -> str:
    """Implement a method to perform basic string compression using the counts
    of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
    "compressed" string would not become smaller than the original string, your method should return
    the original string. You can assume the string has only uppercase and lowercase letters (a - z).
    Hints: #92, #110
    - Do the easy thing first. Compress the string, then compare the lengths.
    - Be careful that you aren't repeatedly concatenating strings together. This can be very inefficient.
    """
    # Kind of an ugly solution...
    if len(input_str) == 0:
        return input_str
    compressed_string = ''
    cur_char = input_str[0]
    cur_count = 0
    for idx, char in enumerate(input_str):
        if char == cur_char:
            cur_count += 1
        elif char != cur_char:
            compressed_string += cur_char
            compressed_string += str(cur_count)
            cur_char = char
            cur_count = 1
        if idx + 1 == len(input_str):
            compressed_string += cur_char
            compressed_string += str(cur_count)
    if len(compressed_string) == 2 * len(input_str):
        return input_str
    return compressed_string


def exc7_rotate_matrix(input_img: List[List]) -> List[List]:
    """Given an image represented by an NxN matrix, where each pixel in the image is 4
    bytes, write a method to rotate the image by 90 degrees. Can you do this in place?
    Hints: #51, # 100
    - Try thinking about it layer by layer. Can you rotate a specific layer?
    - Rotating a specific layer would just mean swapping the values in four arrays. If you were
    asked to swap the values in two arrays, could you do this? Can you then extend it to four arrays?
    """
    pass

