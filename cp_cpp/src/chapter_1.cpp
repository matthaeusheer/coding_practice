//
// Created by matt on 07.11.19.
//

#include <iostream>
#include <unordered_set>  // Hash Set - O(1) insert & access
#include <map>            // Hash Map - O(1) insert & access

#include "chapter_1.h"

/**
 * Given a string of characters, check if they're unique.
 *      Idea: HashSet! Build a O(1) HashSet-lookup, traverse the string and keep adding characters to the set
 *            if the character is not yet in the lookup. Else return False, since we found a duplicate.
 *      Time:   O(n), n length of string, since we have to traverse the whole string. Lookup is constant so doesn't matter.
 *              O(1), if we assume a fixed size character set (like ASCII 128 or ASCII extended 256 or Unicode),
 *                    so the numbers of elements to traverse has an upper fixed bound
 *      Space:  O(1), since size of character set is fixed
 *              O(n, c) if this assumption is not taken, where c = size char set
 */
bool exc1_is_unique(const std::string& str) {
  std::unordered_set<char> lookup = {};
  for (const char& c : str) {
    if (lookup.find(c) == lookup.end()) {
      lookup.insert(c);
    } else {
      return false;
    }
  }
  return true;
}

/**
 * Given two strings, write a method to decide if one is a permutation of the other.
 *      Idea:   What does it mean for two strings to be permuations of each other? It's basically the same characters
 *              arranged in a different way. The key point: Same characters. So the character count for the members
 *              of the string has to be the same for both strings. For that we can use a Hash Map to count the
 *              occurrences of characters in both strings. Then we go through both maps and compare the counts.
 *              If all of them match, we know we have permutations.
 *      Time:   O(n) to go through all elements and then compare afterwards, insert and lookup along the way are O(1)
 *      Space:  O(n) for both has maps
 */
bool exc2_check_permutations(const std::string& first, const std::string& second) {
  std::map<char, int> counts_first, counts_second;

  // Fill up first char counter map
  for (const auto& c : first) {
    if (counts_first.find(c) == counts_first.end()) {
      counts_first[c] = 0;
    } else {
      counts_first[c] += 1;
    }
  }
  // Fill up second char counter map
  for (const auto& c : second) {
    if (counts_second.find(c) == counts_second.end()) {
      counts_second[c] = 0;
    } else {
      counts_second[c] += 1;
    }
  }
  // Compare both char counter maps using range based for loop (could also use iterator syntax)
  for (std::pair<char, int> pair_first : counts_first) {
    char curr_char = pair_first.first;
    char curr_count = pair_first.second;
    if (counts_second.find(curr_char) == counts_second.end()) {
      return false;
    }
    if (counts_second[curr_char] != curr_count) {
      return false;
    }
  }
  return true;
}

/**
 * Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient
 * space at the end to hold the additional characters, and that you are given the "true" length of the string.
 * EXAMPLE
 *   Input: "Mr John Smith     ", 13
 *   Output: "Mr%20John%20Smith"
 *      Idea:   Go through string and count number of whitespaces until we hit the end of the true length of the array.
 *              We need to make true length as a termination criteria because the string is padded at the end with
 *              additional whitespaces for the additional characters. This is used to calculate the index to start from
 *              in the backwards pass in the second step.
 *              In a second pass we start from the back of the string and insert characters starting from end of the
 *              real length string, so we have two indices passing simultaneously. Whenever in the actual string we
 *              encounter a whitespace, we insert %20. Since the idx pointer of the real length string is always in
 *              front of the pointer starting from further back, we can do the replacements in place, this is also
 *              supported by C++ since std::string is mutable (in contrast to java or python where we would have to
 *              use character arrays for example).
 *              Note that if the padding is more than required, the result will have additional white spaces at the end.
 *      Time:   O(n), n total length of string, since we iterate over the loop twice doing constant time operations only
 *      Space:  O(n) to store pairs of indices.
 */
void exc3_urlify(std::string& str, std::size_t real_length) {
  // Step 1 - Count white spaces within real_length bounds.
  std::size_t n_spaces {0};
  for (std::size_t i = 0; i < real_length; i++) {
    if (str[i] == ' ') {
      n_spaces++;
    }
  }
  // Step 2 - Calculate length of new string and starting index for backward loop.
  std::size_t new_length = real_length + 3 * n_spaces - n_spaces;  // Since each white space results in 3 additional characters for %20.
  std::size_t new_idx = new_length;
  for (auto i = real_length; i-- != 0; ) {
    if (str[i] == ' ') {
      str[new_idx - 1] = '0';
      str[new_idx - 2] = '2';
      str[new_idx - 3] = '%';
      new_idx -= 3;
    } else {
      str[new_idx - 1] = str[i];
      new_idx--;
    }
  }
}

/**
 * Given a string, write a function to check if it is a permutation of
 * a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A
 * permutation is a rearrangement of letters. The palindrome does not need to be limited to just
 * dictionary words.
 * EXAMPLE
 *  Input: Tact Coa
 *  Output: True (permutations: "taco cat'; "atc o eta·; etc.)
 *
 * Idea:
 *      What does it mean to be a palindrome? The definition is that it is a word which reads the same when reading
 *      it forward and backwards. A permutation thereof is a word whose letters can be rearranged such that it becomes
 *      a palindrome.
 *      Now, to have that characteristics the string needs to have even character counts for almost all letters such
 *      that half of the occurrences of a character can go on the left and half on the right side. One character is
 *      being allowed to have an odd occurrence count, the one which would go in the middle.
 *      Implementation: We go through the string and fill up a char count hash table. After that we go through
 *      the hash table's content and make sure that at most one character has an odd occurrence count.
 * Time:
 *      O(n), n length of string, to go through it once and then to go through the hash map keys again
 * Space:
 *      O(n), need to store a key/value pair for every distinct character, in worst case they are all unique, so n
 */
bool exc4_palindrome_permutation(const std::string& str) {
  std::map<char, std::size_t> counts;
  for (const char &c : str) {
    if (counts.find(c) != counts.end()) {
      counts[c]++;
    } else {
      counts[c] = 1;
    }
  }
  
  bool found_odd_count {false};
  for (const std::pair<char, std::size_t> pair : counts) {
    if (pair.second % 2 != 0) {
      if (found_odd_count) {
        return false;
      } else {
        found_odd_count = true;
      }
    }
  }
  return true;
}

