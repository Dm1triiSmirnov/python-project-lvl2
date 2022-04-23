import json
import yaml

from gendiff.compare_data import get_diff
from .formatters.formatter import formatter, STYLISH


def read_file(file):
    format = file.split('.')[-1]
    text = file
    if format == 'json':
        with open(text) as json_file:
            data = json.load(json_file)
    elif format == 'yml' or format == 'yaml':
        with open(text) as yml_file:
            data = yaml.safe_load(yml_file)
    return data


def generate_diff(file1, file2, format=STYLISH):
    data1 = read_file(file1)
    data2 = read_file(file2)
    compared_data = get_diff(data1, data2)
    diff = formatter(compared_data, format)
    return diff
