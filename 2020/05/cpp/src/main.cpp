#include "utils.h"

#include <iostream>
#include <fstream>
#include <vector>

int main() {
    std::string filename{"../input"};
    std::ifstream input_file{filename};
    if (!input_file) {
        std::cout << "Input file '" << filename << "' could not be opened!\n";
        return 1;
    }

    int max_seat_id{0};
    std::string current_line;
    std::vector<int> seat_ids;
    while (getline (input_file, current_line)) {
        int const row = utils::get_row (current_line.substr (0, 7));
        int const column = utils::get_column (current_line.substr (7, 3));
        int const current_seat_id = utils::get_seat_id (row, column);
        max_seat_id = current_seat_id > max_seat_id ? current_seat_id : max_seat_id;
        seat_ids.push_back (current_seat_id);
    }

    std::cout << "Solution (part 1): The maximum seat ID is " << max_seat_id << ".\n";

    std::sort (seat_ids.begin (), seat_ids.end ());
    auto it{seat_ids.begin ()};
    while (it != seat_ids.end ()) {
        auto current_value{*it};
        auto next_value{*(it + 1)};

        if ((next_value - current_value) != 1) {
            std::cout << "Solution (part 2): My seat ID is " << current_value + 1 << ".\n";
            break;
        }
        ++it;
    }

    return 0;
}
