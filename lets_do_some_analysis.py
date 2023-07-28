import sys
import os
import pandas as pd
import matplotlib.pyplot as matplot
from scipy.stats import ttest_ind

sys.path.insert(1, os.getcwd()+'/utilities')
from utilities import sql_queries as sq
from utilities import common_functions as cf

def count_by_generations():
    print(sq.pokemon_by_generations)
    generation_count_query = str(sq.pokemon_by_generations)
    generation_count_query_df = pd.read_gbq(generation_count_query, dialect="standard")

    return generation_count_query_df

def generation_stats():
    print(sq.generation_average_stats)
    generation_stats_query = str(sq.generation_average_stats)
    generation_stats_query_df = pd.read_gbq(generation_stats_query, dialect="standard")

    return generation_stats_query_df

def weight_distro_check():
    print(sq.weights_check)
    weight_distro_check_query = str(sq.weights_check)
    weight_distro_check_query_df = pd.read_gbq(weight_distro_check_query, dialect="standard")

    return weight_distro_check_query_df

def gen_7_weight_check():
    print(sq.whats_up_gen_seven)
    gen_7_weight_check_query = str(sq.whats_up_gen_seven)
    gen_7_weight_check_query_df = pd.read_gbq(gen_7_weight_check_query, dialect="standard")

    return gen_7_weight_check_query_df

def weight_distros():
    print('Query is quite long, please check it out in the utilities/sql_queries.py file under the name generation_weight_distros.')
    generation_weight_distros_query = str(sq.generation_weight_distros)
    generation_weight_distros_query_df = pd.read_gbq(generation_weight_distros_query, dialect="standard")

    # Create the plot
    # Create the plot
    cf.generate_plot(0, "Gen 1 Weight Distributions")
    matplot.plot(generation_weight_distros_query_df["pokemon_weight"],
                 generation_weight_distros_query_df["num_gen_1"], label='Gen 1',
                 color='black')

    cf.generate_plot(1, "Gen 2 Weight Distributions")
    matplot.plot(generation_weight_distros_query_df["pokemon_weight"],
                 generation_weight_distros_query_df["num_gen_2"], label='Gen 2',
                 color='black')

    cf.generate_plot(2, "Gen 3 Weight Distributions")
    matplot.plot(generation_weight_distros_query_df["pokemon_weight"],
                 generation_weight_distros_query_df["num_gen_3"], label='Gen 3',
                 color='black')

    cf.generate_plot(3, "Gen 4 Weight Distributions")
    matplot.plot(generation_weight_distros_query_df["pokemon_weight"],
                 generation_weight_distros_query_df["num_gen_4"], label='Gen 4',
                 color='black')

    cf.generate_plot(4, "Gen 5 Weight Distributions")
    matplot.plot(generation_weight_distros_query_df["pokemon_weight"],
                 generation_weight_distros_query_df["num_gen_5"], label='Gen 5',
                 color='black')

    cf.generate_plot(5, "Gen 6 Weight Distributions")
    matplot.plot(generation_weight_distros_query_df["pokemon_weight"],
                 generation_weight_distros_query_df["num_gen_6"], label='Gen 6',
                 color='black')

    cf.generate_plot(6, "Gen 7 Weight Distributions")
    matplot.plot(generation_weight_distros_query_df["pokemon_weight"],
                 generation_weight_distros_query_df["num_gen_7"], label='Gen 7',
                 color='black')

    cf.generate_plot(7, "Gen 8 Weight Distributions")
    matplot.plot(generation_weight_distros_query_df["pokemon_weight"],
                 generation_weight_distros_query_df["num_gen_8"], label='Gen 8',
                 color='black')

    cf.generate_plot(8, "Gen 9 Weight Distributions")
    matplot.plot(generation_weight_distros_query_df["pokemon_weight"],
                 generation_weight_distros_query_df["num_gen_9"], label='Gen 9',
                 color='black')

    matplot.xticks(rotation=90)
    matplot.legend(loc="best")

def weight_ttest_checks():
    print(sq.generation_weight_data('Generation 1'))
    gen_1_query = str(sq.generation_weight_data('Generation 1'))
    gen_1_df = pd.read_gbq(gen_1_query, dialect="standard")

    gen_2_query = str(sq.generation_weight_data('Generation 2'))
    gen_2_df = pd.read_gbq(gen_2_query, dialect="standard")

    gen_3_query = str(sq.generation_weight_data('Generation 3'))
    gen_3_df = pd.read_gbq(gen_3_query, dialect="standard")

    gen_4_query = str(sq.generation_weight_data('Generation 4'))
    gen_4_df = pd.read_gbq(gen_4_query, dialect="standard")

    gen_5_query = str(sq.generation_weight_data('Generation 5'))
    gen_5_df = pd.read_gbq(gen_5_query, dialect="standard")

    gen_6_query = str(sq.generation_weight_data('Generation 6'))
    gen_6_df = pd.read_gbq(gen_6_query, dialect="standard")

    gen_7_query = str(sq.generation_weight_data('Generation 7'))
    gen_7_df = pd.read_gbq(gen_7_query, dialect="standard")

    gen_8_query = str(sq.generation_weight_data('Generation 8'))
    gen_8_df = pd.read_gbq(gen_8_query, dialect="standard")

    gen_9_query = str(sq.generation_weight_data('Generation 9'))
    gen_9_df = pd.read_gbq(gen_9_query, dialect="standard")

    gen_1 = gen_1_df["pokemon_weight"].tolist()
    gen_2 = gen_2_df["pokemon_weight"].tolist()
    gen_3 = gen_3_df["pokemon_weight"].tolist()
    gen_4 = gen_4_df["pokemon_weight"].tolist()
    gen_5 = gen_5_df["pokemon_weight"].tolist()
    gen_6 = gen_6_df["pokemon_weight"].tolist()
    gen_7 = gen_7_df["pokemon_weight"].tolist()
    gen_8 = gen_8_df["pokemon_weight"].tolist()
    gen_9 = gen_9_df["pokemon_weight"].tolist()

    gen_1_to_gen_2_ttest_result = ttest_ind(gen_1, gen_2)
    gen_1_to_gen_3_ttest_result = ttest_ind(gen_1, gen_3)
    gen_1_to_gen_4_ttest_result = ttest_ind(gen_1, gen_4)
    gen_1_to_gen_5_ttest_result = ttest_ind(gen_1, gen_5)
    gen_1_to_gen_6_ttest_result = ttest_ind(gen_1, gen_6)
    gen_1_to_gen_7_ttest_result = ttest_ind(gen_1, gen_7)
    gen_1_to_gen_8_ttest_result = ttest_ind(gen_1, gen_8)
    gen_1_to_gen_9_ttest_result = ttest_ind(gen_1, gen_9)

    print('\nT-Test Results:')
    print('Generation 1 Weights to Generation 2:')
    print('   '+str(gen_1_to_gen_2_ttest_result))
    print('Generation 1 Weights to Generation 3:')
    print('   ' + str(gen_1_to_gen_3_ttest_result))
    print('Generation 1 Weights to Generation 4:')
    print('   ' + str(gen_1_to_gen_4_ttest_result))
    print('Generation 1 Weights to Generation 5:')
    print('   ' + str(gen_1_to_gen_5_ttest_result))
    print('Generation 1 Weights to Generation 6:')
    print('   ' + str(gen_1_to_gen_6_ttest_result))
    print('Generation 1 Weights to Generation 7:')
    print('   ' + str(gen_1_to_gen_7_ttest_result))
    print('Generation 1 Weights to Generation 8:')
    print('   ' + str(gen_1_to_gen_8_ttest_result))
    print('Generation 1 Weights to Generation 9:')
    print('   ' + str(gen_1_to_gen_9_ttest_result))


def height_distro_check():
    print(sq.heights_check)
    height_distro_check_query = str(sq.heights_check)
    height_distro_check_query_df = pd.read_gbq(height_distro_check_query, dialect="standard")

    return height_distro_check_query_df

def height_distros():
    print('Query is quite long, please check it out in the utilities/sql_queries.py file under the name generation_height_distros.')
    generation_height_distros_query = str(sq.generation_height_distros)
    generation_height_distros_query_df = pd.read_gbq(generation_height_distros_query, dialect="standard")

    # Create the plot
    # Create the plot
    cf.generate_plot(9, "Gen 1 Height Distributions")
    matplot.plot(generation_height_distros_query_df["pokemon_height"],
                 generation_height_distros_query_df["num_gen_1"], label='Gen 1',
                 color='black')

    cf.generate_plot(10, "Gen 2 Height Distributions")
    matplot.plot(generation_height_distros_query_df["pokemon_height"],
                 generation_height_distros_query_df["num_gen_2"], label='Gen 2',
                 color='black')

    cf.generate_plot(11, "Gen 3 Height Distributions")
    matplot.plot(generation_height_distros_query_df["pokemon_height"],
                 generation_height_distros_query_df["num_gen_3"], label='Gen 3',
                 color='black')

    cf.generate_plot(12, "Gen 4 Height Distributions")
    matplot.plot(generation_height_distros_query_df["pokemon_height"],
                 generation_height_distros_query_df["num_gen_4"], label='Gen 4',
                 color='black')

    cf.generate_plot(13, "Gen 5 Height Distributions")
    matplot.plot(generation_height_distros_query_df["pokemon_height"],
                 generation_height_distros_query_df["num_gen_5"], label='Gen 5',
                 color='black')

    cf.generate_plot(14, "Gen 6 Height Distributions")
    matplot.plot(generation_height_distros_query_df["pokemon_height"],
                 generation_height_distros_query_df["num_gen_6"], label='Gen 6',
                 color='black')

    cf.generate_plot(15, "Gen 7 Height Distributions")
    matplot.plot(generation_height_distros_query_df["pokemon_height"],
                 generation_height_distros_query_df["num_gen_7"], label='Gen 7',
                 color='black')

    cf.generate_plot(16, "Gen 8 Height Distributions")
    matplot.plot(generation_height_distros_query_df["pokemon_height"],
                 generation_height_distros_query_df["num_gen_8"], label='Gen 8',
                 color='black')

    cf.generate_plot(17, "Gen 9 Height Distributions")
    matplot.plot(generation_height_distros_query_df["pokemon_height"],
                 generation_height_distros_query_df["num_gen_9"], label='Gen 9',
                 color='black')

    matplot.xticks(rotation=90)
    matplot.legend(loc="best")

def height_ttest_checks():
    print(sq.generation_height_data('Generation 1'))
    gen_1_query = str(sq.generation_height_data('Generation 1'))
    gen_1_df = pd.read_gbq(gen_1_query, dialect="standard")

    gen_2_query = str(sq.generation_height_data('Generation 2'))
    gen_2_df = pd.read_gbq(gen_2_query, dialect="standard")

    gen_3_query = str(sq.generation_height_data('Generation 3'))
    gen_3_df = pd.read_gbq(gen_3_query, dialect="standard")

    gen_4_query = str(sq.generation_height_data('Generation 4'))
    gen_4_df = pd.read_gbq(gen_4_query, dialect="standard")

    gen_5_query = str(sq.generation_height_data('Generation 5'))
    gen_5_df = pd.read_gbq(gen_5_query, dialect="standard")

    gen_6_query = str(sq.generation_height_data('Generation 6'))
    gen_6_df = pd.read_gbq(gen_6_query, dialect="standard")

    gen_7_query = str(sq.generation_height_data('Generation 7'))
    gen_7_df = pd.read_gbq(gen_7_query, dialect="standard")

    gen_8_query = str(sq.generation_height_data('Generation 8'))
    gen_8_df = pd.read_gbq(gen_8_query, dialect="standard")

    gen_9_query = str(sq.generation_height_data('Generation 9'))
    gen_9_df = pd.read_gbq(gen_9_query, dialect="standard")

    gen_1 = gen_1_df["pokemon_height"].tolist()
    gen_2 = gen_2_df["pokemon_height"].tolist()
    gen_3 = gen_3_df["pokemon_height"].tolist()
    gen_4 = gen_4_df["pokemon_height"].tolist()
    gen_5 = gen_5_df["pokemon_height"].tolist()
    gen_6 = gen_6_df["pokemon_height"].tolist()
    gen_7 = gen_7_df["pokemon_height"].tolist()
    gen_8 = gen_8_df["pokemon_height"].tolist()
    gen_9 = gen_9_df["pokemon_height"].tolist()

    gen_1_to_gen_2_ttest_result = ttest_ind(gen_1, gen_2)
    gen_1_to_gen_3_ttest_result = ttest_ind(gen_1, gen_3)
    gen_1_to_gen_4_ttest_result = ttest_ind(gen_1, gen_4)
    gen_1_to_gen_5_ttest_result = ttest_ind(gen_1, gen_5)
    gen_1_to_gen_6_ttest_result = ttest_ind(gen_1, gen_6)
    gen_1_to_gen_7_ttest_result = ttest_ind(gen_1, gen_7)
    gen_1_to_gen_8_ttest_result = ttest_ind(gen_1, gen_8)
    gen_1_to_gen_9_ttest_result = ttest_ind(gen_1, gen_9)

    print('\nT-Test Results:')
    print('Generation 1 Heights to Generation 2:')
    print('   '+str(gen_1_to_gen_2_ttest_result))
    print('Generation 1 Heights to Generation 3:')
    print('   ' + str(gen_1_to_gen_3_ttest_result))
    print('Generation 1 Heights to Generation 4:')
    print('   ' + str(gen_1_to_gen_4_ttest_result))
    print('Generation 1 Heights to Generation 5:')
    print('   ' + str(gen_1_to_gen_5_ttest_result))
    print('Generation 1 Heights to Generation 6:')
    print('   ' + str(gen_1_to_gen_6_ttest_result))
    print('Generation 1 Heights to Generation 7:')
    print('   ' + str(gen_1_to_gen_7_ttest_result))
    print('Generation 1 Heights to Generation 8:')
    print('   ' + str(gen_1_to_gen_8_ttest_result))
    print('Generation 1 Heights to Generation 9:')
    print('   ' + str(gen_1_to_gen_9_ttest_result))

