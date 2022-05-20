'''INF 211 - Project 3 - EuroLeague

Make sure it can get imported, and no syntax errors in your code for any
credit.
'''

my_name = "Furkan Cayci"
my_id = "12345678"
my_email = "furkancayci@gtu.edu.tr"


class Person:
    '''Person class'''
    pass


class Player:
    '''Player class that will inherit from Person class'''
    pass


class Manager:
    '''Manager class that will inherit from Person class'''
    pass


class Team:
    '''Team class'''
    pass


class Match:
    '''Match class'''
    pass


class Season:
    '''Season class'''
    pass


if __name__ == "__main__":

    teams_file = 'teams.txt'
    managers_file = 'managers.txt'
    players_file = 'players.txt'

    # Create a season
    season21 = Season(teams_file, managers_file, players_file)

    # Play the matches
    for i in range(season21.get_season_length()):
        season21.play_week()

    # Get season statistics
    print("Champion is:", season21.get_champion() )
    print("Most scoring team is:", season21.get_most_scoring_team() )
    print("Best player is:", season21.get_best_player() )
    print("Best manager is:", season21.get_best_manager() )
