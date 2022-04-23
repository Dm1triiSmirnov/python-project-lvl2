import os
import pytest

from gendiff.gen_diff import generate_diff
from gendiff.formatters.formatter import STYLISH, PLAIN, JSON


def read_file(file_name):
    return os.path.join(os.path.dirname(__file__), 'fixtures', file_name)


def read_result_file(file_name):
    file = os.path.join(os.path.dirname(__file__), 'fixtures/test_results', file_name)
    with open(file) as result:
        return ''.join(result.readlines())


FLAT_JSON_FILE_1 = read_file('flat_file1.json')
FLAT_JSON_FILE_2 = read_file('flat_file2.json')
FLAT_YAML_FILE_1 = read_file('flat_file1.yaml')
FLAT_YAML_FILE_2 = read_file('flat_file2.yaml')

NESTED_JSON_FILE_1 = read_file('nested_file1.json')
NESTED_JSON_FILE_2 = read_file('nested_file2.json')
NESTED_YAML_FILE_1 = read_file('nested_file1.yaml')
NESTED_YAML_FILE_2 = read_file('nested_file2.yaml')

RESULT_FLAT = read_result_file('test_result_flat.txt')
RESULT_STYLISH = read_result_file('test_result_stylish_formatter.txt')
RESULT_JSON = read_result_file('test_result_json_formatter.txt')
RESULT_PLAIN = read_result_file('test_result_plain_formatter.txt')


@pytest.mark.parametrize('file_1, file_2, expected_result, formatter', [
    (FLAT_JSON_FILE_1, FLAT_JSON_FILE_2, RESULT_FLAT, STYLISH),
    (FLAT_YAML_FILE_1, FLAT_YAML_FILE_2, RESULT_FLAT, STYLISH),
    (NESTED_JSON_FILE_1, NESTED_JSON_FILE_2, RESULT_STYLISH, STYLISH),
    (NESTED_YAML_FILE_1, NESTED_YAML_FILE_2, RESULT_STYLISH, STYLISH),
    (NESTED_JSON_FILE_1, NESTED_JSON_FILE_2, RESULT_PLAIN, PLAIN),
    (NESTED_YAML_FILE_1, NESTED_YAML_FILE_2, RESULT_PLAIN, PLAIN),
    (NESTED_JSON_FILE_1, NESTED_JSON_FILE_2, RESULT_JSON, JSON),
    (NESTED_YAML_FILE_1, NESTED_YAML_FILE_2, RESULT_JSON, JSON),
])
def test_generate_diff(file_1, file_2, expected_result, formatter):
    assert generate_diff(file_1, file_2, formatter) == expected_result
