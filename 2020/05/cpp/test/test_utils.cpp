#include <gtest/gtest.h>
#include <utility>
#include "../src/utils.h"

class StringIntParam : public ::testing::TestWithParam<std::pair<std::string, int>> {
};

class GetRow : public StringIntParam {
};


TEST_P(GetRow, examples_from_description) {
    auto const&[input_str, expected_result] = GetParam ();
    ASSERT_EQ(utils::get_row (input_str), expected_result);
}

INSTANTIATE_TEST_SUITE_P(utils, GetRow, ::testing::Values (
        std::pair<std::string, int>{"FBFBBFF", 44},
        std::pair<std::string, int>{"BFFFBBF", 70},
        std::pair<std::string, int>{"FFFBBBF", 14},
        std::pair<std::string, int>{"BBFFBBF", 102}
));

class GetColumn : public StringIntParam {
};


TEST_P(GetColumn, examples_from_description) {
    auto const&[input_str, expected_result] = GetParam ();
    ASSERT_EQ(utils::get_column (input_str), expected_result);
}

INSTANTIATE_TEST_SUITE_P(utils, GetColumn, ::testing::Values (
        std::pair<std::string, int>{"RLR", 5},
        std::pair<std::string, int>{"RRR", 7},
        std::pair<std::string, int>{"RLL", 4}
));

class IntIntIntParam : public ::testing::TestWithParam<std::tuple<int, int, int>> {
};

class GetSeatId : public IntIntIntParam {
};


TEST_P(GetSeatId, examples_from_description) {
    auto const&[row, column, expected_result] = GetParam ();
    ASSERT_EQ(utils::get_seat_id (row, column), expected_result);
}

INSTANTIATE_TEST_SUITE_P(utils, GetSeatId, ::testing::Values (
        std::tuple<int, int, int>{44, 5, 357},
        std::tuple<int, int, int>{70, 7, 567},
        std::tuple<int, int, int>{102, 4, 820}
));

class IntIntParam : public ::testing::TestWithParam<std::pair<int, int>> {
};

class Pow2 : public IntIntParam {
};


TEST_P(Pow2, sanity_check) {
    auto const&[exp, expected_result] = GetParam ();
    ASSERT_EQ(utils::pow_2 (exp), expected_result);
}

INSTANTIATE_TEST_SUITE_P(utils, Pow2, ::testing::Values (
        std::pair<int, int>{1, 2},
        std::pair<int, int>{2, 4},
        std::pair<int, int>{3, 8},
        std::pair<int, int>{7, 128}
));
