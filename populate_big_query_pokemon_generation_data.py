import pandas as pd

import sys
import os
sys.path.insert(1, os.getcwd()+'/utilities')

from utilities import table_management as tm

def insert_data_values():
    table_name = 'rahman-portfolio.pokedex.pokemon_generations'
    column_names = 'generation_name, start_pokemon_num, ending_pokemon_num'
    clean_out_query = tm.pokemon_table_clean_out(table_name)

    load_query = tm.pokemon_load_table(table_name, column_names, tm.populate_pokemon_generation_values())

    cleaning_out_data = pd.read_gbq(clean_out_query, dialect="standard")
    load_query = pd.read_gbq(load_query, dialect="standard")

insert_data_values()