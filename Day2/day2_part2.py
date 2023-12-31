""" https://adventofcode.com/2023/day/2#part2 The power of a set of cubes is equal to the numbers of red, green, and blue cubes multiplied together. The power of the minimum set of cubes in game 1 is 48. In games 2-5 it was 12, 1560, 630, and 36, respectively. Adding up these five powers produces the sum 2286.

For each game, find the minimum set of cubes that must have been present. What is the sum of the power of these sets?

input example: Game 1: 7 red, 8 blue; 6 blue, 6 red, 2 green; 2 red, 6 green, 8 blue; 9 green, 2 red, 4 blue; 6 blue, 4 green
"""

def parse_games(game_set: str) -> list[dict]:
    """
    Parses a game set string and returns a list of dictionaries representing each game.

    Args:
        game_set (str): The game set string to be parsed.

    Returns:
        list[dict]: A list of dictionaries representing each game. Each dictionary contains the color of the cube as the key and the number as the value.
    """
    games_list = game_set.split(";")
    game_dict_list = []
    for game_str in games_list:
        game_dict = {}
        rounds = game_str.split(",")
        if game_str.startswith("Game"):
            rounds.pop(0)
        for round_str in rounds:
            number, color_cube = round_str.strip().split()
            game_dict[color_cube] = int(number)
        game_dict_list.append(game_dict)
    return game_dict_list

def get_maxdict(game: list[dict]) -> dict:
    """
    Calculates the maximum value for each color cube in a game.

    Args:
        game (list[dict]): A list of dictionaries representing each round of the game.

    Returns:
        dict: A dictionary containing the maximum value for each color cube.
    """
    max_dict = {"red": 0, "green": 0, "blue": 0}
    for round in game:
        for color_cube in round.keys():
            if round[color_cube] > max_dict[color_cube]:
                max_dict[color_cube] = round[color_cube]
    return max_dict

def get_powercube(game_cubes: dict) -> int:
    """
    Calculates the powercube by multiplying all the values in the given dictionary.

    Args:
        game_cubes (dict): A dictionary containing the game cubes and their values.

    Returns:
        int: The calculated powercube.
    """
    powercube = 1
    for value in game_cubes.values():
        powercube *= value
    return powercube
        

def find_sum_cubespower(input: str) -> int:
    """
    Calculates the sum of the power cubes for each game in the input file.

    Args:
        input (str): The path to the input file.

    Returns:
        int: The sum of the power cubes.
    """
    with open(input) as f:
        lines = f.readlines()
        sum = 0
        for line in lines:
            game = parse_games(line)
            max_dict = get_maxdict(game)
            sum += get_powercube(max_dict)
    return sum

if __name__ == "__main__":
    print(find_sum_cubespower("input.txt"))
    