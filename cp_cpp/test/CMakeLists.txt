# ----- Executable for chapter 1 unit test -----
add_executable(
        test_chapter_1
        test_chapter_1.cpp
)

target_link_libraries(
        test_chapter_1
        gtest_main
        chapter1_lib
)

add_test(
        NAME
        unit
        COMMAND
        ${CMAKE_BINARY_DIR}/${CMAKE_INSTALL_BINDIR}/unit_tests
)