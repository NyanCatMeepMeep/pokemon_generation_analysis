def pokemon_table_clean_out(full_table_name):
    query = """
delete from `"""+full_table_name+"""` where 1=1
"""
    return query

def pokemon_load_table(full_table_name, columns, values_to_load):
    query = """
insert into `"""+full_table_name+"""` ("""+columns+""")
values """+values_to_load

    return query

def populate_pokemon_generation_values():
    query = """
    ('Generation 1', 1, 151),
    ('Generation 2', 152,251),
    ('Generation 3', 252,386),
    ('Generation 4', 387,493),
    ('Generation 5', 494,649),
    ('Generation 6', 650,721),
    ('Generation 7', 722,809),
    ('Generation 8', 810,905),
    ('Generation 9', 906,1016)
"""

    return query