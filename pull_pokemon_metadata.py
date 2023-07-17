import requests

import sys
import os
sys.path.insert(1, os.getcwd()+'/utilities')

import utilities.common_functions as cf
import utilities.table_management as tm

def fetch_data(pokemon_id):
    pokemon_list= 'https://pokeapi.co/api/v2/pokemon/'+str(pokemon_id)
    pokemon = requests.get(pokemon_list)
    pokemon_pretty = pokemon.json()
    return pokemon_pretty

def build_values_insertion():
    num_pokemon = 1010
    on_pokemon = 1
    full_values_insertion = ''

    output_file_location = cf.output_file_path() + cf.set_output_file_name()
    output_file_contents = cf.open_file(output_file_location)


    while on_pokemon <= num_pokemon:
        print("Fetching data for pokemon number: " + str(on_pokemon))
        pokemon_collection = fetch_data(on_pokemon)

        pokemon_number = pokemon_collection['id']
        pokemon_name = pokemon_collection['name']
        pokemon_height = pokemon_collection['height']
        pokemon_weight = pokemon_collection['weight']
        pokemon_base_hp = pokemon_collection['stats'][0]['base_stat']
        pokemon_base_attack = pokemon_collection['stats'][1]['base_stat']
        pokemon_base_defence = pokemon_collection['stats'][2]['base_stat']
        pokemon_base_special_attack = pokemon_collection['stats'][3]['base_stat']
        pokemon_base_special_defence = pokemon_collection['stats'][4]['base_stat']
        pokemon_base_speed = pokemon_collection['stats'][5]['base_stat']

        insertion_string = str(pokemon_number) + ',' + \
                           cf.format_string_for_ingestion(cf.remove_escape_characters(str(pokemon_name))) + ',' +\
                           str(pokemon_height) + ',' + \
                           str(pokemon_weight) + ',' + \
                           str(pokemon_base_hp) + ',' + \
                           str(pokemon_base_attack) + ',' + \
                           str(pokemon_base_defence) + ',' + \
                           str(pokemon_base_special_attack) + ',' + \
                           str(pokemon_base_special_defence) + ',' + \
                           str(pokemon_base_speed)

        if on_pokemon != num_pokemon:
            insertion_string_ready = cf.form_values_string(insertion_string)+',\n'
        else:
            insertion_string_ready = cf.form_values_string(insertion_string)

        output_file_contents.write(insertion_string_ready)
        output_file_contents.flush()

        on_pokemon = on_pokemon + 1

    output_file_contents.close()

    return full_values_insertion

build_values_insertion()

