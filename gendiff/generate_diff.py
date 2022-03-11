import json
import yaml
from gendiff.parse_data import parse_data


def get_data(file):
    if file.split('.')[-1] == 'json':
        return json.load(open(file))
    elif file.split('.')[-1] == 'yml' or file.split('.')[-1] == 'yaml':
        with open(file) as yml_file:
            return yaml.safe_load(yml_file)


def generate_diff(file1, file2):
    data1 = get_data(file1)
    data2 = get_data(file2)
    diff = parse_data(data1, data2)
    return diff
