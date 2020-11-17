# ----- Data Structures Library -----
add_library(data_structs_lib)
target_sources(data_structs_lib
        PRIVATE
        data_structures.cpp
        PUBLIC
        ${CMAKE_CURRENT_SOURCE_DIR}/data_structures.h
        )

# ----- Data Structure Executable -----
add_executable(data_structs_main
        data_structures_main.cpp)

target_link_libraries(data_structs_main
        data_structs_lib)