import requests

base_url = "https://pokeapi.co/api/v2/pokemon"

def get_pokemon_info(name):
    url = f"{base_url}/{name}"
    response = requests.get(url)
    
    if response.status_code == 200:
        # print('connected successfully')
        return response.json()
    else:
        print('Could not connect to the url')
        return None

pokemon_name = input("Enter pokemon name: ")

get_info = get_pokemon_info(pokemon_name)

if get_info:
    print(f"\nName : {get_info['name'].capitalize()}.")
    print(f"Height : {get_info['height']}")
    print(f"Base Experience : {get_info['base_experience']}")
