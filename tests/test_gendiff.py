import os
import pytest

from gendiff.gen_diff import generate_diff
from gendiff.formatters.formatter import STYLISH, PLAIN, JSON


FLAT_JSON_FILE_1 = 'flat_file1.json'
FLAT_JSON_FILE_2 = 'flat_file2.json'
FLAT_YAML_FILE_1 = 'flat_file1.yaml'
FLAT_YAML_FILE_2 = 'flat_file2.yaml'

NESTED_JSON_FILE_1 = 'nested_file1.json'
NESTED_JSON_FILE_2 = 'nested_file2.json'
NESTED_YAML_FILE_1 = 'nested_file1.yaml'
NESTED_YAML_FILE_2 = 'nested_file2.yaml'

RESULT_FLAT = 'test_result_flat.txt'
RESULT_STYLISH = 'test_result_stylish_formatter.txt'
RESULT_JSON = 'test_result_json_formatter.txt'
RESULT_PLAIN = 'test_result_plain_formatter.txt'


def read_file(file_name):
    return os.path.join(os.path.dirname(__file__), 'fixtures', file_name)


def read_result_file(file_name):
    file = os.path.join(os.path.dirname(__file__), 'fixtures/test_results', file_name)
    with open(file) as result:
        return ''.join(result.readlines())

@pytest.mark.parametrize('file_name_1, file_name_2, result_file_name, formatter', [
    (FLAT_JSON_FILE_1, FLAT_JSON_FILE_2, RESULT_FLAT, STYLISH),
    (FLAT_YAML_FILE_1, FLAT_YAML_FILE_2, RESULT_FLAT, STYLISH),
    (NESTED_JSON_FILE_1, NESTED_JSON_FILE_2, RESULT_STYLISH, STYLISH),
    (NESTED_YAML_FILE_1, NESTED_YAML_FILE_2, RESULT_STYLISH, STYLISH),
    (NESTED_JSON_FILE_1, NESTED_JSON_FILE_2, RESULT_PLAIN, PLAIN),
    (NESTED_YAML_FILE_1, NESTED_YAML_FILE_2, RESULT_PLAIN, PLAIN),
    (NESTED_JSON_FILE_1, NESTED_JSON_FILE_2, RESULT_JSON, JSON),
    (NESTED_YAML_FILE_1, NESTED_YAML_FILE_2, RESULT_JSON, JSON),
])
def test_generate_diff(file_name_1, file_name_2, result_file_name, formatter):
    file_1 = read_file(file_name_1)
    file_2 = read_file(file_name_2)
    expected_result = read_result_file(result_file_name)
    assert generate_diff(file_1, file_2, formatter) == expected_result
