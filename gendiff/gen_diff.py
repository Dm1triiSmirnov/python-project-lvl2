import json
import yaml

from gendiff.compare_data import get_diff
from .formatters.formatter import formatter, STYLISH


def read_file(file_path):
    file_format = file_path.split('.')[-1]
    with open(file_path) as file:
        text = file.read()
        return text, file_format


def parse_file(text, file_format):
    if file_format == 'json':
        parsed_data = json.loads(text)
    elif file_format == 'yml' or file_format == 'yaml':
        parsed_data = yaml.safe_load(text)
    return parsed_data


def generate_diff(file_path1, file_path2, format=STYLISH):
    text1, file_format1 = read_file(file_path1)
    text2, file_format2 = read_file(file_path2)
    parsed_data1 = parse_file(text1, file_format1)
    parsed_data2 = parse_file(text2, file_format2)
    compared_data = get_diff(parsed_data1, parsed_data2)
    diff = formatter(compared_data, format)
    return diff
