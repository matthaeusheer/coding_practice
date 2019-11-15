#include <iostream>
#include <string>

template <typename T>
std::string l_or_r_value(T&&) {
  return std::is_lvalue_reference<T>{} ? "LVALUE!" : "RVALUE!";
}

int g = 10;
int foo() { return 1; }                       // ok
int& bar() { int a = 1; return a; }           // ERROR: Reference to stack memory with local variable, idiot!
                                              // error only during runtime, compiler is ok with that
int dip() { return g; }                       // ok
int& dip_ref() { return g; }                  // ok
// int&& r_ref() { return g; }                // ERROR: cannot bind ‘int’ lvalue to ‘int&&’, compiler complains
int&& r_ref_move() { return std::move(g); }   // Clang-Tidy gives warning to remove move on trivially copyable int type
int&& r_ref_move2() { return 1; }             // Returning ref to temporary local object, runtime error

int main() {
  std::cout << "foo()         " << l_or_r_value(foo()) << std::endl;
  std::cout << "bar()         " << l_or_r_value(bar()) << std::endl;
  // std::cout << "bar()         " << bar() << std::endl; // runtime error
  std::cout << "dip()         " << l_or_r_value(dip()) << std::endl;
  std::cout << "dip_ref()     " << l_or_r_value(dip_ref()) << std::endl;
  std::cout << "r_ref_move()  " << l_or_r_value(r_ref_move()) << std::endl;
  std::cout << "r_ref_move2() " << l_or_r_value(r_ref_move2()) << std::endl;
  // std::cout << "r_ref_move2() " << r_ref_move2() << std::endl; // runtime error
}