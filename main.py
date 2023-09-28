"""
main.py: Fetch MLB Team Data by ID

This module provides functionalities to fetch detailed data for an MLB team based on its team ID. 
The data is sourced from the MLB-StatsAPI, and the module offers a command-line interface for user input.

Functions:
    - fetch_team_data_by_id(team_id: int) -> dict:
        Fetches all available data for a specific MLB team using its ID.

Usage:
    Run the script and provide the MLB team ID when prompted. 
    The script will fetch and display the available data keys for the given team ID.

Example:
    $ python main.py
    Enter the ID of the MLB team: 133
    Data keys for team ID 133: ['copyRight', 'queryResults']

Note:
    - Ensure the MLB-StatsAPI package is installed and properly set up before running this script.
    - The script assumes valid input (an integer representing a team ID) and does not handle non-integer input gracefully.
"""


import statsapi
import datetime

def fetch_todays_games():
    # Get today's date
    today = datetime.date.today().strftime('%Y-%m-%d')
    yesterday = (datetime.date.today() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
        
    try:
        # Fetch the schedule for today
        schedule = statsapi.schedule(date=yesterday)
    except statsapi.utils.APIError as e:
        print(f"API Error: {e}")
        return
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return
    
    if not schedule:
        print(f"No games scheduled for {today}.")
        return

    for game in schedule:
        try:
            print_game_info(game)
        except Exception as e:
            print(f"Failed to process game data. Error: {e}")

def print_game_info(game):
    game_id = game['game_id']
    away_team = game['away_name']
    home_team = game['home_name']
    
    game_status = game.get('status', "Not Started")
    
    print(f"{away_team} vs. {home_team} - Status: {game_status}")
    
    # If the game has concluded, print the scores or more detailed stats
    if game_status == "Final":
        print(f"{away_team} Score: {game['away_score']}")
        print(f"{home_team} Score: {game['home_score']}")
        # You can fetch more detailed stats using statsapi.boxscore_data(game_id) if needed

if __name__ == "__main__":
    try:
        fetch_todays_games()
    except Exception as e:
        print(f"An unexpected error occurred while fetching today's games: {e}")

