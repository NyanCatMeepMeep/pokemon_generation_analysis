import glob
import pandas as pd

import sys
import os
sys.path.insert(1, os.getcwd()+'/utilities')

from utilities import table_management as tm
import utilities.common_functions as cf

def insert_data_values():
    table_name = 'rahman-portfolio.pokedex.pokemon_base_metadata'
    column_names = 'pokemon_id, pokemon_name, pokemon_height, pokemon_weight, pokemon_base_hp, pokemon_base_attack, pokemon_base_defence, pokemon_base_special_attack, pokemon_base_special_defence, pokemon_base_speed'
    clean_out_query = tm.pokemon_table_clean_out(table_name)


    current_list_of_result_files = glob.glob(str(cf.output_file_path())+'*')
    latest_file = max(current_list_of_result_files, key=os.path.getctime)

    result_file = open(latest_file)
    values_to_insert = result_file.read()

    load_query = tm.pokemon_load_table(table_name, column_names, values_to_insert)

    cleaning_out_data = pd.read_gbq(clean_out_query, dialect="standard")
    load_query = pd.read_gbq(load_query, dialect="standard")

insert_data_values()