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

fn solve_part1(jolt_ratings_input: &Vec<i32>) -> (usize, usize) {
    let mut full_jolt_ratings = jolt_ratings_input.to_vec();
    full_jolt_ratings.push(0); // charging outlet
    full_jolt_ratings.push(full_jolt_ratings.iter().max().unwrap() + 3); // built-in joltage adapter
    full_jolt_ratings.sort();

    let jolt_diffs = full_jolt_ratings.windows(2)
        .map(|slice| slice[1] - slice[0])
        .collect::<Vec<_>>();

    (count_if(&jolt_diffs, 1), count_if(&jolt_diffs, 3))
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
    println!("Part 1:\n\
              \tThe number of 1-jolt differences multiplied by the number of 3-jolt\n\
              \tdifferences is {}.", one_jolt_diffs * three_jolt_diffs);
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
            28,
            33,
            18,
            42,
            31,
            14,
            46,
            20,
            48,
            47,
            24,
            23,
            49,
            45,
            19,
            38,
            39,
            11,
            1,
            32,
            25,
            35,
            8,
            17,
            7,
            9,
            4,
            2,
            34,
            10,
            3
        ];
        assert_eq!(solve_part1(&input), (22, 10));
    }
}
