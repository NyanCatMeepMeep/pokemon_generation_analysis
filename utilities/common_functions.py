import os
import datetime

def form_values_string(string):
    result = "("+string+")"

    return result

def format_string_for_ingestion(string):
    formatted_string = "'"+string+"'"

    return formatted_string
def remove_escape_characters(string):
    string_clean = string.replace("'",'')

    return string_clean

def find_path():
    curr_path=os.getcwd()
    return curr_path

def output_file_path():
    root_path = os.path.dirname(os.getcwd())
    directory = 'output_files'
    output_path = root_path+'/pokemon_gotta_catch_em_all/'+directory+'/'
    return output_path

def set_output_file_name():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H_%M_%S")
    file_name = 'Pokemon_pull' + '_' + timestamp
    return file_name


def open_file(file_path_and_name):
    output_file = open(file_path_and_name,"a+")
    return output_file