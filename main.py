import requests

def fetch_pokemon_data():
    api_url = "https://pokeapi.co/api/v2/pokemon?limit=1025"
    response = requests.get(api_url)
    
    if response.status_code == 200:
        data = response.json()
        return [(index + 1, pokemon['name'].capitalize()) for index, pokemon in enumerate(data['results'])]
    else:
        raise Exception("Failed to fetch Pokémon data")

def generate_pokedex_wikitable(pokemon_list, output_file):
    wikicode = '{| class="wikitable sortable"\n! # !! Pokémon !! Location\n'

    for pokemon_id, name in pokemon_list:
        wikicode += f'|-\n| {pokemon_id} || [[File:{name}.png|50px]] {name} || None\n'

    wikicode += '|}'

    with open(output_file, "w", encoding="utf-8") as file:
        file.write(wikicode)
    
    print(f"Wikitable successfully saved to {output_file}.")

try:
    pokemon_data = fetch_pokemon_data()
    generate_pokedex_wikitable(pokemon_data, "pokedex_wikitable.txt")
except Exception as e:
    print(f"An error occurred: {e}")
