import json
import yaml

from gendiff.parse_data import parse_data
from .formatters.formatter import formatter


def get_data(file):
    extension = file.split('.')[-1]
    if extension == 'json':
        with open(file) as json_file:
            data = json.load(json_file)
    elif extension == 'yml' or extension == 'yaml':
        with open(file) as yml_file:
            data = yaml.safe_load(yml_file)
    return data


def generate_diff(file1, file2, format='stylish'):
    data1 = get_data(file1)
    data2 = get_data(file2)
    compared_data = parse_data(data1, data2)
    diff = formatter(compared_data, format)
    return diff
