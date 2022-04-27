import os
import json
import yaml

from gendiff.compare_data import get_diff
from .formatters.formatter import formatter, STYLISH


def read_file(file_path):
    format = os.path.splitext(file_path)[-1].lstrip('.')
    with open(file_path) as file:
        text = file.read()
        return text, format


def parse(text, format):
    if format == 'json':
        parsed_data = json.loads(text)
    elif format == 'yml' or format == 'yaml':
        parsed_data = yaml.safe_load(text)
    return parsed_data


def generate_diff(file_path1, file_path2, format=STYLISH):
    text1, file_format1 = read_file(file_path1)
    text2, file_format2 = read_file(file_path2)
    parsed_data1 = parse(text1, file_format1)
    parsed_data2 = parse(text2, file_format2)
    compared_data = get_diff(parsed_data1, parsed_data2)
    diff = formatter(compared_data, format)
    return diff
