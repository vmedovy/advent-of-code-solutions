#![warn(clippy::all)]

use std::fs;

const SEAT_EMPTY: char = 'L';
const SEAT_OCCUPIED: char = '#';

fn print_banner(msg: &str) {
    let sep_length = msg.len() + 2;
    println!("+{}+", "-".repeat(sep_length));
    println!("| {} |", msg);
    println!("+{}+", "-".repeat(sep_length));
}

struct Point {
    x: usize,
    y: usize,
}

fn count_total_occupied_seats(seating_area: &[Vec<char>]) -> usize {
    let mut counter = 0usize;
    for row in seating_area {
        for col in row {
            if *col == SEAT_OCCUPIED {
                counter += 1;
            }
        }
    }
    counter
}

fn count_adjacent_occupied_seats(seating_area: &[Vec<char>], p: &Point) -> usize {
    let mut counter = 0usize;

    let mut adjacent_seats: Vec<Point> = Vec::with_capacity(8);
    for y_offset in -1..=1 {
        let y_seat = p.y as i32 + y_offset;
        if y_seat < 0 || y_seat >= seating_area.len() as i32 {
            continue;
        }

        for x_offset in -1..=1 {
            let x_seat = p.x as i32 + x_offset;
            if (x_offset == 0 && y_offset == 0)
                || x_seat < 0
                || x_seat >= seating_area[y_seat as usize].len() as i32
            {
                continue;
            }

            adjacent_seats.push(Point {
                x: x_seat as usize,
                y: y_seat as usize,
            });
        }
    }

    for seat in adjacent_seats {
        if seating_area[seat.y][seat.x] == SEAT_OCCUPIED {
            counter += 1;
        }
    }
    counter
}

fn solve_part1(seating_area: &[Vec<char>]) -> usize {
    let mut curr_state = seating_area.to_vec();
    let mut next_state = seating_area.to_vec();
    loop {
        for row in 0..curr_state.len() {
            for col in 0..curr_state[row].len() {
                let curr_seat = curr_state[row][col];
                let adjacent_occupied_seat_count =
                    count_adjacent_occupied_seats(&curr_state, &Point { x: col, y: row });
                if curr_seat == SEAT_EMPTY && adjacent_occupied_seat_count == 0 {
                    next_state[row][col] = SEAT_OCCUPIED;
                } else if curr_seat == SEAT_OCCUPIED && adjacent_occupied_seat_count >= 4 {
                    next_state[row][col] = SEAT_EMPTY;
                }
            }
        }

        if next_state == curr_state {
            break;
        }

        curr_state = next_state.to_vec();
    }

    count_total_occupied_seats(&curr_state)
}

fn main() {
    print_banner("Advent of Code - Day 11: Seating System");

    let seat_layout = fs::read_to_string("../input")
        .expect("Could not read input file!")
        .split_whitespace()
        .filter(|e| *e != "")
        .map(|e| e.to_string().chars().collect::<Vec<_>>())
        .collect::<Vec<_>>();

    println!(
        "Part 1:\n\
         \tAfter simulating the seating area by applying the seating rules repeatedly until no\n\
         \tseats change state, {} seats end up occupied.",
        solve_part1(&seat_layout)
    );
}

#[cfg(test)]
mod part1 {
    use super::*;

    #[test]
    fn test_example() {
        let input = vec![
            "L.LL.LL.LL",
            "LLLLLLL.LL",
            "L.L.L..L..",
            "LLLL.LL.LL",
            "L.LL.LL.LL",
            "L.LLLLL.LL",
            "..L.L.....",
            "LLLLLLLLLL",
            "L.LLLLLL.L",
            "L.LLLLL.LL",
        ];
        assert_eq!(
            solve_part1(
                &input
                    .iter()
                    .map(|e| e.to_string().chars().collect::<Vec<_>>())
                    .collect::<Vec<_>>()
            ),
            37
        );
    }
}
