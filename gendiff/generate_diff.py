import json
from gendiff.parse_data import parse_data


def generate_diff(file1, file2):
    data1 = json.load(open(file1))
    data2 = json.load(open(file2))
    diff = parse_data(data1, data2)
    return diff
