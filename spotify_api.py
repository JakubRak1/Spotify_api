import requests


SPOTIFY_ACCESS_TOKEN = ''
SPOTIFY_GET_CURRENT_TRACK_URL = 'https://api.spotify.com/v1/me/player'


def get_current_track(access_token):
    # Autohrize user to spotify and get need information and store in variables
    response = requests.get(SPOTIFY_GET_CURRENT_TRACK_URL, headers={"Authorization": f"Bearer {access_token}"})
    resp_json = response.json()
    track_name:str = resp_json['item']['name']
    artists:list = resp_json['item']['artists']
    artists_names:str = ', '.join([artist['name'] for artist in artists])
    # Join multiply artist as one string
    link:str = resp_json['item']['external_urls']['spotify']


    current_track_info:dict = {
        "name": track_name,
        "artists": artists_names, 
        "link": link
    }
    return current_track_info
    # Create current_track_info dict with needed informations

def main():
    # Main function that prints basic informations
    current_track_info:dict = get_current_track(SPOTIFY_ACCESS_TOKEN)
    print(f"Title: {current_track_info['name']}")
    print(f"Created by: {current_track_info['artists']}")
    print(f"Link to song: {current_track_info['link']}")


if __name__ == "__main__":
    main()