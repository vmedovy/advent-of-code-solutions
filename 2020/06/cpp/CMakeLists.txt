cmake_minimum_required(VERSION 3.17)

SET(PUZZLE_YEAR 2020)
SET(PUZZLE_DAY 6)

project(advent-of-code_${PUZZLE_YEAR}-${PUZZLE_DAY})
set(CMAKE_CXX_STANDARD 20)

add_executable(${PROJECT_NAME}_part1 src/main_part1.cpp)
