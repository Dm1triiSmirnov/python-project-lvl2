import os
import pytest

from gendiff.gen_diff import generate_diff


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

@pytest.mark.parametrize('file_1, file_2, expected_result, formatter', [
    (read_file(FLAT_JSON_FILE_1), read_file(FLAT_JSON_FILE_2), read_result_file(RESULT_FLAT), 'stylish'),
    (read_file(FLAT_YAML_FILE_1), read_file(FLAT_YAML_FILE_2), read_result_file(RESULT_FLAT), 'stylish'),
    (read_file(NESTED_JSON_FILE_1), read_file(NESTED_JSON_FILE_2), read_result_file(RESULT_STYLISH), 'stylish'),
    (read_file(NESTED_YAML_FILE_1), read_file(NESTED_YAML_FILE_2), read_result_file(RESULT_STYLISH), 'stylish'),
    (read_file(NESTED_JSON_FILE_1), read_file(NESTED_JSON_FILE_2), read_result_file(RESULT_PLAIN), 'plain'),
    (read_file(NESTED_YAML_FILE_1), read_file(NESTED_YAML_FILE_2), read_result_file(RESULT_PLAIN), 'plain'),
    (read_file(NESTED_JSON_FILE_1), read_file(NESTED_JSON_FILE_2), read_result_file(RESULT_JSON), 'json'),
    (read_file(NESTED_YAML_FILE_1), read_file(NESTED_YAML_FILE_2), read_result_file(RESULT_JSON), 'json'),
])


def test_gendiff(file_1, file_2, expected_result, formatter):
    assert generate_diff(file_1, file_2, formatter) == expected_result
