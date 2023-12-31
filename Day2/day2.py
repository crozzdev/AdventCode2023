""" https://adventofcode.com/2023/day/2 Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes. What is the sum of the IDs of those games?

input example: Game 1: 7 red, 8 blue; 6 blue, 6 red, 2 green; 2 red, 6 green, 8 blue; 9 green, 2 red, 4 blue; 6 blue, 4 green

"""

BAG = {"red": 12, "green": 13, "blue": 14}

def get_gameid(game_set: str) -> int:
    """
    Extracts the game ID from a game set string.

    Parameters:
    game_set (str): The game set string in the format "GameID: GameData".

    Returns:
    int: The extracted game ID.

    """
    game_id = game_set.split(":")[0]
    game_number_id = int(game_id.split()[1])
    return game_number_id

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
    for index in range(len(games_list)):
        game_dict = {}
        game_list = games_list[index].split(",")
        if index == 0:
            game_list[0] = game_list[0].split(":")[1]
        for round in game_list:
            round_split = round.split()
            number = round_split[0]
            color_cube = round_split[1]
            game_dict[color_cube] = number
        game_dict_list.append(game_dict)
    return game_dict_list
            
            
def check_game(game: list[dict]) -> bool:
    """
    Checks if a game is possible with the cubes in the bag.

    Args:
        game (list[dict]): The game to be checked. This is a list of dicts, where each dict represent a round.

    Returns:
        bool: True if the game is possible, False otherwise.
    """
    
    for round in game:
        for color_cube in round.keys():
            if int(round[color_cube]) > BAG[color_cube]:
                return False
    return True

def find_sum_ids(input: str) -> int:
    """
    Calculates the sum of game IDs that meet certain conditions.

    Parameters:
    input (str): The path to the input file.

    Returns:
    int: The sum of game IDs.

    """
    with open(input) as f:
        lines = f.readlines()
        sum = 0
        for line in lines:
            game_set = parse_games(line)
            if check_game(game_set):
                sum += get_gameid(line)
    return sum

if __name__ == "__main__":
    print(find_sum_ids("input.txt"))

           
        