#include <iostream>
#include <vector>
#include <string>
#include "chapter_1.h"

const std::string SEPARATOR = "= = = = = = = = = =";

int main() {

  // ----- Exc 1 "Is Unique" -----
  std::cout << SEPARATOR << std::endl;
  std::cout << "\tEXERCISE 1 - Is Unique" << std::endl;
  std::cout << "Exc1: Is Unique." << std::endl;
  std::vector<std::string> strings = {"a", "aa", "abcde", "", "abbc"};
  for (const auto& str : strings) {
    std::string result = exc1_is_unique(str) ? "Yes!" : "No.";
    std::cout << "Is \"" << str << "\" unique? " << result << std::endl;
  }
  std::cout << SEPARATOR << std::endl;

  // ----- Exc 2 "Check Permutations" -----
  std::cout << SEPARATOR << std::endl;
  std::cout << "\tEXERCISE 2 - Check Permutation" << std::endl;

}