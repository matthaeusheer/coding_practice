# ----- Chapter 1 Library -----
add_library(chapter1_lib "")

target_sources(chapter1_lib
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

# ----- Data Structures Library -----
add_library(data_structs_lib "")
target_sources(data_structs_lib
        PRIVATE
        data_structures.cpp
        PUBLIC
        ${CMAKE_CURRENT_LIST_DIR}/data_structures.h
)
target_include_directories(
        data_structs_lib
        PUBLIC
        ${CMAKE_CURRENT_LIST_DIR}
)

# ----- Data Structure Executable -----
add_executable(data_structs_main
        data_structures_main.cpp)

target_link_libraries(data_structs_main
        data_structs_lib)

# ----- Tryout Executable -----
add_executable(tryout_main
        tryout_main.cpp)
