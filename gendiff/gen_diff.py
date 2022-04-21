import json
import yaml

from gendiff.compare_data import get_diff
from .formatters.formatter import formatter, STYLISH


def read_file(file):
    extension = file.split('.')[-1]
    file_name = file
    return file_name, extension


def parse_file(file_name, extension):
    if extension == 'json':
        with open(file_name) as json_file:
            data = json.load(json_file)
    elif extension == 'yml' or extension == 'yaml':
        with open(file_name) as yml_file:
            data = yaml.safe_load(yml_file)
    return data


def generate_diff(file1, file2, format=STYLISH):
    file1_name, extension1 = read_file(file1)
    file2_name, extension2 = read_file(file2)
    data1 = parse_file(file1_name, extension1)
    data2 = parse_file(file2_name, extension2)
    compared_data = get_diff(data1, data2)
    diff = formatter(compared_data, format)
    return diff
