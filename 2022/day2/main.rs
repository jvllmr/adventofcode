use std::collections::HashMap;
use std::fs;

fn read_file() -> String {
    return fs::read_to_string("input.txt").expect("Wo Datei?");
}

fn get_rounds() -> Vec<(String, String)> {
    let input = read_file();
    let lines = input.split("\n");
    let mut rounds: Vec<(String, String)> = Vec::new();

    for line in lines {
        let mut players = line.split(" ");

        let player1 = players.next();
        let player2 = players.next();
        rounds.push((
            player1.expect("Wo Wert?").to_string(),
            player2.expect("Wo Wert?").to_string(),
        ))
    }

    return rounds;
}

fn play_round(round: (&str, &str)) -> i32 {
    let value_map: HashMap<&str, i32> =
        HashMap::from([("A", 1), ("B", 2), ("C", 3), ("X", 1), ("Y", 2), ("Z", 3)]);

    let (player1, player2) = round;
    let player1_value: i32 = value_map.get(&player1).unwrap().clone();
    let player2_value: i32 = value_map.get(&player2).unwrap().clone();

    let mut win = 6;

    if (player1_value > player2_value && !(player1_value == 3 && player2_value == 1))
        || (player1_value == 1 && player2_value == 3)
    {
        win = 0;
    } else if player1_value == player2_value {
        win = 3;
    }

    return win + player2_value;
}

fn matchfix(round: (&str, &str)) -> i32 {
    let value_map: HashMap<&str, i32> =
        HashMap::from([("A", 1), ("B", 2), ("C", 3), ("X", 1), ("Y", 2), ("Z", 3)]);
    let (opponent_play, expected_outcome) = round;
    let opponent_play_value = value_map.get(&opponent_play).unwrap().clone();
    if expected_outcome == "Y" {
        return 3 + value_map.get(&opponent_play).unwrap();
    }

    if expected_outcome == "X" {
        if opponent_play_value == 1 {
            return 3;
        }
        return opponent_play_value - 1;
    }

    if opponent_play_value == 3 {
        return 7;
    }
    return 6 + opponent_play_value + 1;
}

fn main() {
    let rounds = get_rounds();
    let mut score = 0;

    for round in rounds.iter() {
        let (player1, player2) = round;
        let round_score = play_round((player1, player2));
        score = score + round_score;
    }

    println!("{}", score);
    score = 0;
    for round in rounds.iter() {
        let (player1, player2) = round;
        let round_score = matchfix((player1, player2));
        score = score + round_score;
    }
    println!("{}", score);
}
