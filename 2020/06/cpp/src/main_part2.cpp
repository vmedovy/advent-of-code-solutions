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
    std::vector<size_t> common_answer_count;
    std::set<char> common_answers;
    bool first_answer{true};
    auto finalize_group = [&]() {
        common_answer_count.push_back(common_answers.size());
        common_answers.clear();
        first_answer = true;
    };
    while (getline(input_file, current_line)) {
        if (current_line.empty()) {
            finalize_group();
            continue;
        }
        if (first_answer) {
            common_answers.insert(current_line.cbegin(), current_line.cend());
            first_answer = false;
        } else {
            std::set<char> next_answers(current_line.begin(), current_line.end());
            std::set<char> intersection;
            std::set_intersection(common_answers.begin(), common_answers.end(),
                                  next_answers.begin(), next_answers.end(),
                                  std::inserter(intersection, intersection.begin()));
            common_answers = intersection;
        }
    }
    finalize_group();

    size_t const common_answers_sum = std::accumulate(common_answer_count.cbegin(), common_answer_count.cend(), 0UL);
    std::cout << "Solution (part 2): The sum of common answers per group is " << common_answers_sum << ".\n";

    return 0;
}
