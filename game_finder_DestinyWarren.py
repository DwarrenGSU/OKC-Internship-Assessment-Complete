"""
Given the following inputs:
- <game_data> is a list of dictionaries, with each dictionary representing a player's shot attempts in a game. The list can be empty, but any dictionary in the list will include the following keys: gameID, playerID, gameDate, fieldGoal2Attempted, fieldGoal2Made, fieldGoal3Attempted, fieldGoal3Made, freeThrowAttempted, freeThrowMade. All values in this dictionary are ints, except for gameDate which is of type str in the format 'MM/DD/YYYY'
- <true_shooting_cutoff> is the minimum True Shooting percentage value for a player to qualify in a game. It will be an int value >= 0.
- <player_count> is the number of players that need to meet the <true_shooting_cutoff> in order for a gameID to qualify. It will be an int value >= 0.

Implement find_qualified_games to return a list of unique qualified gameIDs in which at least <player_count> players have a True Shooting percentage >= <true_shooting_cutoff>, ordered from most to least recent game.
"""

def find_qualified_games(game_data: list[dict], true_shooting_cutoff: int, player_count: int) -> list[int]:
	# Replace the line below with your code
	from datetime import datetime

def calculate_true_shooting_percentage(player_data: dict) -> float:
    # Extract necessary stats from player data
    field_goal2_made = player_data['fieldGoal2Made']
    field_goal2_attempted = player_data['fieldGoal2Attempted']
    field_goal3_made = player_data['fieldGoal3Made']
    field_goal3_attempted = player_data['fieldGoal3Attempted']
    free_throw_made = player_data['freeThrowMade']
    free_throw_attempted = player_data['freeThrowAttempted']
    
    # Calculate points scored
    points_scored = 2 * field_goal2_made + 3 * field_goal3_made + free_throw_made
    
    # Calculate total field goal attempts
    total_fga = field_goal2_attempted + field_goal3_attempted
    
    # Calculate True Shooting attempts
    tsa = total_fga + 0.44 * free_throw_attempted
    
    # Return TS% (handle the case when TSA is zero)
    if tsa == 0:
        return 0
    return (points_scored / (2 * tsa)) * 100

def find_qualified_games(game_data: list[dict], true_shooting_cutoff: int, player_count: int) -> list[int]:
    # Dictionary to store the number of qualified players per gameID
    qualified_games = {}
    
    # Iterate over all player game records
    for player_game in game_data:
        game_id = player_game['gameID']
        game_date = player_game['gameDate']
        
        # Calculate the player's true shooting percentage
        ts_percentage = calculate_true_shooting_percentage(player_game)
        
        # Check if the player qualifies based on the true_shooting_cutoff
        if ts_percentage >= true_shooting_cutoff:
            if game_id not in qualified_games:
                qualified_games[game_id] = {'count': 0, 'gameDate': game_date}
            qualified_games[game_id]['count'] += 1
    
    # Filter out games where the number of qualified players is less than player_count
    qualified_game_ids = [
        game_id for game_id, data in qualified_games.items() if data['count'] >= player_count
    ]
    
    # Sort the games by gameDate in descending order
    qualified_game_ids.sort(key=lambda game_id: datetime.strptime(qualified_games[game_id]['gameDate'], '%m/%d/%Y'), reverse=True)
    
    return qualified_game_ids
game_data = [
    {'gameID': 1, 'playerID': 101, 'gameDate': '09/15/2023', 'fieldGoal2Attempted': 5, 'fieldGoal2Made': 3, 'fieldGoal3Attempted': 4, 'fieldGoal3Made': 2, 'freeThrowAttempted': 2, 'freeThrowMade': 1},
    {'gameID': 1, 'playerID': 102, 'gameDate': '09/15/2023', 'fieldGoal2Attempted': 7, 'fieldGoal2Made': 4, 'fieldGoal3Attempted': 5, 'fieldGoal3Made': 3, 'freeThrowAttempted': 3, 'freeThrowMade': 2},
    {'gameID': 2, 'playerID': 101, 'gameDate': '09/14/2023', 'fieldGoal2Attempted': 4, 'fieldGoal2Made': 2, 'fieldGoal3Attempted': 6, 'fieldGoal3Made': 1, 'freeThrowAttempted': 1, 'freeThrowMade': 0},
]

true_shooting_cutoff = 55
player_count = 1

print(find_qualified_games(game_data, true_shooting_cutoff, player_count))
