#include "utils.h"

namespace utils {
    int pow_2(unsigned long exp) {
        int result{1};
        while (exp--) {
            result *= 2;
        }
        return result;
    }

    inline int resolve_binary_space_partitioning(std::string const &specifier, char lower_half, char upper_half) {
        int current_subtractor{pow_2 (specifier.length () - 1)};
        int lower_border{0}, upper_border{pow_2 (specifier.length ())};
        for (auto const c : specifier) {
            if (c == lower_half)
                upper_border -= current_subtractor;
            else if (c == upper_half)
                lower_border += current_subtractor;
            current_subtractor /= 2;
        }
        return lower_border;
    }

    int get_row(std::string const &row_specifier) {
        return resolve_binary_space_partitioning(row_specifier, 'F', 'B');
    }

    int get_column(std::string const &column_specifier) {
        return resolve_binary_space_partitioning(column_specifier, 'L', 'R');;
    }

    int get_seat_id(int const row, int const column) {
        return row * 8 + column;
    }
}
