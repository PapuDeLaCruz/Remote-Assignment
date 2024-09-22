"""
Fabian De La Cruz
andrez.delacruz@gmail.com
Given the following inputs:
- <game_data> is a list of dictionaries, with each dictionary representing a player's shot attempts in a game. The list can be empty, 
but any dictionary in the list will include the following keys: 
    gameID, int
	playerID, int
	gameDate, str[MM/DD/YYYY]
	fieldGoal2Attempted, int
	fieldGoal2Made, int
	fieldGoal3Attempted, int 
	fieldGoal3Made, int
	freeThrowAttempted, int 
	freeThrowMade. int
All values in this dictionary are ints, except for gameDate which is of type str in the format 'MM/DD/YYYY'
- <true_shooting_cutoff> is the minimum True Shooting percentage value for a player to qualify in a game. It will be an int value >= 0.
- <player_count> is the number of players that need to meet the <true_shooting_cutoff> in order for a gameID to qualify. 
    It will be an int value >= 0.

Implement find_qualified_games to return a list of unique qualified gameIDs in which at least <player_count> players have a 
True Shooting percentage >= <true_shooting_cutoff>, ordered from most to least recent game.
"""
def find_qualified_games(game_data: list[dict], true_shooting_cutoff: int, player_count: int) -> list[int]:

    true_shooting_percentage = lambda data: 100 * (2 * data['fieldGoal2Made'] + 3 * data['fieldGoal3Made']+data['freeThrowMade']) / (2 * (data['fieldGoal2Attempted'] + data['fieldGoal3Attempted'] + (0.44 * data['freeThrowAttempted'])))
    #lambda function to calculate true shooting percentage as it is brief but will be reused. Could also be included/ directly in the main for loop.
    #I initially had this as a separate function but I think it is more concise this way
    #it could also be included directly in the main for loop but I think it is more readable this way

    qualified_games_ids = []
    #list to store the gameIDs that meet both conditions

    counter = {}
    #dictionary to store the gameID and the number of players that meet the true shooting percentage cutoff
    

    for game in game_data:
        if true_shooting_percentage(game) >= true_shooting_cutoff:
            if game['gameID'] in counter:
                counter[game['gameID']] += 1
            else:
                counter[game['gameID']] = 1
    #for loop to iterate over the game_data and check if the true shooting percentage is greater than the cutoff and

    for key, value in counter.items():
        if value >= player_count:
            qualified_games_ids.append(key)
    #for loop to iterate over the dictionary and append the gameIDs that meet the player count condition to the list

    #these for loops could be lambda functions but I think it is more readable this way

    return qualified_games_ids


"""
for game in game_data:
    if true_shooting_percentage(game) >= true_shooting_cutoff:
        if game['gameID'] in counter:
            counter[game['gameID']] += 1
            if counter[game['gameID']] >= player_count:
                if game['gameID'] not in qualified_games_ids:
                    qualified_games_ids.append(game['gameID'])
        else:
            counter[game['gameID']] = 1
            if counter[game['gameID']] >= player_count:
                if game['gameID'] not in qualified_games_ids:
                    qualified_games_ids.append(game['gameID'])
"""

#this is the same as the previous for loops but it is all in one loop. it is more concise, but it has a worse performance due to
#it checking if the game is not in the list every time. With a big list of all qualified games it would be o(n^2) instead of o(n)




