#ifndef ADVENT_OF_CODE_2020_5_UTILS_H
#define ADVENT_OF_CODE_2020_5_UTILS_H

#include <string>

namespace utils {
    int pow_2(unsigned long exp);

    int get_row(std::string const &row_specifier);

    int get_column(std::string const &column_specifier);

    int get_seat_id(int const row, int const column);
}

#endif
