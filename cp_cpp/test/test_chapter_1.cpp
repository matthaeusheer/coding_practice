#include "gtest/gtest.h"

#include "chapter_1.h"

// ========== EXERCISE 1 ========== //

TEST(TestExc1, TestIsUnique) {
  ASSERT_EQ(exc1_is_unique("abcde"), true);
  ASSERT_EQ(exc1_is_unique("a"), true);
  ASSERT_EQ(exc1_is_unique("aa"), false);
  ASSERT_EQ(exc1_is_unique(""), true);
  ASSERT_EQ(exc1_is_unique("abbc"), false);
}

TEST(TestExc2, CheckPermutations) {
  ASSERT_EQ(exc2_check_permutations("abc", "cba"), true);
  ASSERT_EQ(exc2_check_permutations("a", "a"), true);
  ASSERT_EQ(exc2_check_permutations("", ""), true);
  ASSERT_EQ(exc2_check_permutations("abcdd", "ddbac"), true);
  ASSERT_EQ(exc2_check_permutations("abcddf", "ddbac"), false);
  ASSERT_EQ(exc2_check_permutations("abcddff", "dbacf"), false);
}

TEST(TestExc3, Urlify) {
  std::string in_str = "Hello World!  ";
  ASSERT_EQ(exc3_urlify(in_str, 12), "Hello%20World!");

}