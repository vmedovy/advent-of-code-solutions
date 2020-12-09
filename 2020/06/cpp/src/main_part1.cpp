#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <numeric>

int main() {
    std::string filename{"../input"};
    std::ifstream input_file{filename};
    if (!input_file) {
        std::cout << "Input file '" << filename << "' could not be opened!\n";
        return 1;
    }

    std::string current_line;
    std::vector<size_t> unique_answer_count;
    std::set<char> unique_answers;
    auto finalize_group = [&]() {
        unique_answer_count.push_back(unique_answers.size());
        unique_answers.clear();
    };
    while (getline(input_file, current_line)) {
        if (current_line.empty()) {
            finalize_group();
            continue;
        }
        unique_answers.insert(current_line.cbegin(), current_line.cend());
    }
    finalize_group();

    size_t const unique_answers_sum = std::accumulate(unique_answer_count.cbegin(), unique_answer_count.cend(), 0UL);
    std::cout << "Solution (part 1): The sum of unique answers per group is " << unique_answers_sum << ".\n";

    return 0;
}
