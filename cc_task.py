import sys
import requests
import json
from urllib.parse import urljoin

def get_my_pokemon(pokemon_name):  #This function i have used to get the pokemon details
 
    base_url = "https://pokeapi.co/api/v2/pokemon/"
    url = urljoin(base_url, pokemon_name.lower())  #The api url is created through base url and then path parameter is added to it
    response = requests.get(url)
    if response.status_code == 200:  # if the status is OK
        pokemon_data = response.json()
        types = [i['type']['name'].capitalize() for i in pokemon_data['types']]
        print(f"National Number:{pokemon_data['id']}")
        print(f"Type: {', '.join(types)}")
        print(f"Name: {pokemon_data['name']}")
        print(f"Height: {pokemon_data['height']/10}m")
        print(f"Weight: {pokemon_data['weight']/10}kg")
        print(f"Abilities:")
        for ability in pokemon_data['abilities']:
            print(f" - {ability['ability']['name']}")
        print("Base Stats:")
        total=0
        for stat in pokemon_data['stats']:
            stat_name = stat['stat']['name'].capitalize()
            base_stat = stat['base_stat']
            total+=stat['base_stat']
            print(f" - {stat_name}: {base_stat}")
        print("Total",total)
        sprite_url = pokemon_data['sprites']['other']['official-artwork']['front_default']
        download_image(sprite_url)

    elif response.status_code == 404:
        print(f"Error:Pokemon '{pokemon_name}' details  not found.")
    else:
        print(f"Error:Sorry.We couldnt fetch the details. Status code {response.status_code}")

def download_image(url):  #This function i have made to download the image
    response = requests.get(url)
    if response.status_code == 200:
        # Save the image to sprite.png
        with open("sprite.png", "wb") as sprite_file:
            sprite_file.write(response.content)
        print(" image downloaded and saved as sprite.png")
    else:
        print(f"Failed to download  image with Status code {response.status_code}")

if __name__ == "__main__":
    if len(sys.argv) != 2:  #to check if correct argument is passed or not
        print("wrong arguments")
        sys.exit(1)

    pokemon_name = sys.argv[1]
    get_my_pokemon(pokemon_name)
