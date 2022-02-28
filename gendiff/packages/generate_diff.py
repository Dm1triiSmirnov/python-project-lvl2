import json
from gendiff.packages.parse_data import parse_data


def generate_diff(file_path1, file_path2):
    data1 = json.load(open(file_path1))
    data2 = json.load(open(file_path2))
    diff = parse_data(data1, data2)
    return diff





