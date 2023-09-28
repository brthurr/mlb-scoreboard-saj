import statsapi
import requests
import cairosvg

def fetch_team_data_by_id(team_id):
    """
    Fetch all available data for a specific MLB team by its ID and downloads the team logo, converting it to PNG.
    
    Args:
    - team_id (int): The ID of the MLB team.
    
    Returns:
    - dict: A dictionary containing all available data for the specified team.
    """
    try:
        # Validate if the provided ID corresponds to an MLB team
        teams = statsapi.get('teams', {'sportIds': 1})
        if not any(team['id'] == team_id for team in teams['teams']):
            print(f"No team found with the ID {team_id}.")
            return None

        # Fetch all data for the team using its ID
        team_data = statsapi.get('team', {'teamId': team_id})

        # Download and convert the logo
        download_and_convert_logo(team_id)

        return team_data

    except statsapi.utils.APIError as e:
        print(f"API Error: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

def download_and_convert_logo(team_id):
    """Downloads the team logo from the MLB website, converts it from SVG to PNG, and resizes it to 32x32."""
    logo_url = f"https://www.mlbstatic.com/team-logos/{team_id}.svg"
    
    try:
        response = requests.get(logo_url)
        response.raise_for_status()

        # Convert the SVG content to PNG
        png_bytes = cairosvg.svg2png(bytestring=response.content, output_width=32, output_height=32)

        # Save the PNG
        with open(f"team_{team_id}.png", "wb") as png_file:
            png_file.write(png_bytes)
        
        print(f"Logo saved as team_{team_id}.png")

    except requests.RequestException as e:
        print(f"Error fetching logo: {e}")
    except cairosvg.Error as e:
        print(f"Error converting SVG to PNG: {e}")

if __name__ == "__main__":
    team_id = int(input("Enter the ID of the MLB team: "))
    data = fetch_team_data_by_id(team_id)
    if data:
        # For demonstration purposes, we're just printing the keys of the data.
        print(f"Data keys for team ID {team_id}: {list(data.keys())}")

