# ----- Chapter 1 Library -----
add_library(chapter1_lib "")

target_sources(
        chapter1_lib
        PRIVATE
        chapter_1.cpp
        PUBLIC
        ${CMAKE_CURRENT_LIST_DIR}/chapter_1.h
)

target_include_directories(
        chapter1_lib
        PUBLIC
        ${CMAKE_CURRENT_LIST_DIR}
)

# ----- Chapter 1 Executable -----
add_executable(
        chapter_1_main
        chapter_1_main.cpp)

target_link_libraries(chapter_1_main
        chapter1_lib)