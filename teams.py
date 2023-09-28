import statsapi
import json

def fetch_teams_to_json(filename="teams.json"):
    try:
        # Fetch all MLB teams
        teams = statsapi.get('teams', {'sportIds': 1})

        # Extract the team names and IDs
        team_data = [
            {"id": team['id'], "name": team['name']}
            for team in teams['teams']
        ]

        # Save the data to a JSON file
        with open(filename, 'w') as f:
            json.dump(team_data, f, indent=4)
        
        print(f"Data saved to {filename}")

    except statsapi.utils.APIError as e:
        print(f"API Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    fetch_teams_to_json()

