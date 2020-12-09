#include "utils.h"

#include <iostream>
#include <fstream>

int main() {
    std::string filename{"../input"};
    std::ifstream input_file{filename};
    if (!input_file) {
        std::cout << "Input file '" << filename << "' could not be opened!\n";
        return 1;
    }

    int max_seat_id{0};
    std::string current_line;
    while (getline (input_file, current_line)) {
        int const row = utils::get_row (current_line.substr (0, 7));
        int const column = utils::get_column (current_line.substr (7, 3));
        int const current_seat_id = utils::get_seat_id (row, column);

        max_seat_id = current_seat_id > max_seat_id ? current_seat_id : max_seat_id;
    }

    std::cout << "Solution (part 1): The maximum seat ID is " << max_seat_id << ".\n";
    return 0;
}
