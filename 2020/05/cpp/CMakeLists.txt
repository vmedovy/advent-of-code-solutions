cmake_minimum_required(VERSION 3.17)

SET(PUZZLE_YEAR 2020)
SET(PUZZLE_DAY 5)

project(advent-of-code_${PUZZLE_YEAR}-${PUZZLE_DAY})
set(CMAKE_CXX_STANDARD 20)

add_library(${PROJECT_NAME}_utils src/utils.h src/utils.cpp)

add_executable(${PROJECT_NAME} src/main.cpp)
target_link_libraries(${PROJECT_NAME} ${PROJECT_NAME}_utils)

find_package(GTest CONFIG REQUIRED)
add_executable(${PROJECT_NAME}_UT test/main_UT.cpp test/test_utils.cpp)
target_link_libraries(${PROJECT_NAME}_UT GTest::gtest ${PROJECT_NAME}_utils)