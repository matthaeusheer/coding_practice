# coding_practice

This repo is the place where I sharpen my algorithms & data structure coding skills. Algorithms, Data Structures and Coding Interview Questions.
The repo holds code in different languages, such as Python, C++ and Java.

## Python

### Code Structure
```
cp_python/
  algorithms/
    A selection of interesting algorithms.
  cracking_coding_interview/
    Solutions to interview questions from Cracking the Coding Interview (utilizes data_structures package).
  data_structures
    Most common data structures implementations. 
  random_questions/
    Some interesting stuff I came along and solved it here.
  tests/
    Unit tests for all packages listed above.
```
### Installation
I recommend using ```pyenv``` to manage your python versions along with ```pipenv``` to manage your dependencies in a clean virtual environment. Since most of this stuff is pretty basic, there are not a lot of dependencies used throughout this package. I recommend Python >3.7 to deal with extensive type hinting I use (supported for Python >3.5).

### Running the Tests
Inside ```cp_python``` run ```python -m unittest discover``` to run all tests. You should get something like
```
----------------------------------------------------------------------
Ran 45 tests in 0.009s

OK
```
if all tests passed.

## C++
### Code Structure
```
cp_cpp/
  src/
    ...source files...
    CMakeLists.txt
    [Holds all source code (TODO: split into sub-packages and src/ include/ dirs if this grows larger).]
  tests/
    ...test source files...
    CMakeLists.txt
    [Unit tests using Google Test.]
```
### Installation
Make sure to have CMake >3.5 and a decent C++ compiler installed, e.g. GNU 5.4. All dependencies (such as Google Test) are handled by the CMakeLists.txt files in place. To build the project do (inside ```cp_cpp```)
```
mkdir build
cd build
cmake ..
make
```
### Running the tests
To run the tests, go to the ```cd <PATH_TO_REPO>/cp_cpp/build/test/``` and run a test executable, e.g. ```./test_chapter_1``` which should give you 
```
[==========] Running 4 tests from 4 test suites.
[----------] Global test environment set-up.
[----------] 1 test from TestExc1
[ RUN      ] TestExc1.TestIsUnique
[       OK ] TestExc1.TestIsUnique (0 ms)
[----------] 1 test from TestExc1 (0 ms total)

[----------] 1 test from TestExc2
[ RUN      ] TestExc2.CheckPermutations
[       OK ] TestExc2.CheckPermutations (0 ms)
[----------] 1 test from TestExc2 (0 ms total)

[----------] 1 test from TestExc3
[ RUN      ] TestExc3.Urlify
[       OK ] TestExc3.Urlify (0 ms)
[----------] 1 test from TestExc3 (0 ms total)

[----------] 1 test from TestExc4
[ RUN      ] TestExc4.PalindromePermutation
[       OK ] TestExc4.PalindromePermutation (0 ms)
[----------] 1 test from TestExc4 (0 ms total)

[----------] Global test environment tear-down
[==========] 4 tests from 4 test suites ran. (0 ms total)
[  PASSED  ] 4 tests.
```

## Java
Coming soon.
