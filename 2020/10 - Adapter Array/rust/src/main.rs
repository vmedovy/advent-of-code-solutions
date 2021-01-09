#![warn(clippy::all)]

use std::fs;
use std::str::FromStr;

fn print_banner(msg: &str) {
    let sep_length = msg.len() + 2;
    println!("+{}+", "-".repeat(sep_length));
    println!("| {} |", msg);
    println!("+{}+", "-".repeat(sep_length));
}

fn count_if(vec: &Vec<i32>, val: i32) -> usize {
    vec.iter().filter(|x| **x == val).count()
}

fn calculate_joltage_differences(jolt_ratings_input: &Vec<i32>) -> Vec<i32> {
    let mut full_jolt_ratings = jolt_ratings_input.to_vec();
    full_jolt_ratings.push(0); // charging outlet
    full_jolt_ratings.push(full_jolt_ratings.iter().max().unwrap() + 3); // built-in joltage adapter
    full_jolt_ratings.sort();

    full_jolt_ratings
        .windows(2)
        .map(|slice| slice[1] - slice[0])
        .collect::<Vec<_>>()
}

fn solve_part1(jolt_ratings_input: &Vec<i32>) -> (usize, usize) {
    let jolt_diffs = calculate_joltage_differences(jolt_ratings_input);

    (count_if(&jolt_diffs, 1), count_if(&jolt_diffs, 3))
}

fn solve_part2(jolt_ratings_input: &Vec<i32>) -> usize {
    let joltage_differences = calculate_joltage_differences(jolt_ratings_input);
    let joltage_difference_sequence_lengths = joltage_differences
        .split(|val| *val == 3)
        .map(|block| block.len())
        .collect::<Vec<_>>();

    //-------------------------------------------------------
    // verify assumptions that were made for simple solution
    //-------------------------------------------------------
    // Assuming that the only existing joltage differences are 1 and 3 means that joltage difference
    // sequences split at joltage differences of 3 only consist of 1s.
    assert!(joltage_differences
        .iter()
        .all(|elem| *elem == 1 || *elem == 3));

    // Assuming a maximum sequence length of 4 and sequences consisting of only 1s allows to count
    // the possible options manually:
    // * sequence length 0 -> 0 options -> not relevant
    // * sequence length 1 -> 1 option  -> not relevant
    // * sequence length 2 -> 2 options
    //   * 11
    //   * 2
    // * sequence length 3 -> 4 options
    //   * 111
    //   * 12
    //   * 21
    //   * 3
    // * sequence length 4 -> 7 options
    //   * 1111
    //   * 211
    //   * 121
    //   * 112
    //   * 31
    //   * 13
    //   * 22
    assert!(*joltage_difference_sequence_lengths.iter().max().unwrap() <= 4);

    joltage_difference_sequence_lengths
        .iter()
        .filter(|seq_len| **seq_len > 1)
        .fold(1, |prod: usize, seq_len: &usize| {
            prod * match *seq_len {
                2 => 2,
                3 => 4,
                4 => 7,
                _ => panic!("Unexpected sequence length of {}!", seq_len),
            }
        })
}

fn main() {
    print_banner("Advent of Code - Day 10: Adapter Array");

    let input_filepath = "../input";
    let jolt_ratings = fs::read_to_string(input_filepath)
        .expect("Could not read input file!")
        .split('\n')
        .filter(|e| *e != "")
        .map(|num| i32::from_str(num).unwrap())
        .collect::<Vec<_>>();

    let (one_jolt_diffs, three_jolt_diffs) = solve_part1(&jolt_ratings);
    println!(
        "Part 1:\n\
         \tThe number of 1-jolt differences multiplied by the number of 3-jolt\n\
         \tdifferences is {}.",
        one_jolt_diffs * three_jolt_diffs
    );
    println!(
        "Part 2:\n\
         \tThe number of possible combinations is {}.",
        solve_part2(&jolt_ratings)
    );
}

#[cfg(test)]
mod part1 {
    use super::*;

    #[test]
    fn test_count_if() {
        let input = vec![1, 2, 2, 3, 3, 3];
        assert_eq!(count_if(&input, 1), 1);
        assert_eq!(count_if(&input, 2), 2);
        assert_eq!(count_if(&input, 3), 3);
    }

    #[test]
    fn test_first_example() {
        let input = vec![16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4];
        assert_eq!(solve_part1(&input), (7, 5));
    }

    #[test]
    fn test_second_example() {
        let input = vec![
            28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49, 45, 19, 38, 39, 11, 1, 32, 25, 35,
            8, 17, 7, 9, 4, 2, 34, 10, 3,
        ];
        assert_eq!(solve_part1(&input), (22, 10));
    }
}

#[cfg(test)]
mod part2 {
    use super::*;

    #[test]
    fn test_first_example() {
        let input = vec![16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4];
        assert_eq!(solve_part2(&input), 8);
    }

    #[test]
    fn test_second_example() {
        let input = vec![
            28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49, 45, 19, 38, 39, 11, 1, 32, 25, 35,
            8, 17, 7, 9, 4, 2, 34, 10, 3,
        ];
        assert_eq!(solve_part2(&input), 19208);
    }
}
