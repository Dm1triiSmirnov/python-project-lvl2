import json
from gendiff.parse_data import parse_data
import os


def generate_diff(file1, file2):
    file_path1 = os.path.abspath(file1)
    file_path2 = os.path.abspath(file2)
    data1 = json.load(open(file_path1))
    data2 = json.load(open(file_path2))
    diff = parse_data(data1, data2)
    return diff
