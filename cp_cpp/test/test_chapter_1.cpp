#include "gtest/gtest.h"

#include "chapter_1.h"

TEST(TestChapter1, TestAddTwoNumbers) {
  ASSERT_EQ(add(1, 2), 3);
}