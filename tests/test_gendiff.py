import os

from gendiff.generate_diff import generate_diff


def test_gediff_flat_json():
    file1 = os.path.join(os.path.dirname(__file__), 'fixtures', 'flat_file1.json')
    file2 = os.path.join(os.path.dirname(__file__), 'fixtures', 'flat_file2.json')
    with open(os.path.join(os.path.dirname(__file__), 'fixtures', 'test_result_flat_json.txt')) as result:
        test_result = ''.join(result.readlines())
    assert generate_diff(file1, file2) == test_result


def test_gendiff_json_stylish():
    file1 = os.path.join(os.path.dirname(__file__), 'fixtures', 'nested_file1.json')
    file2 = os.path.join(os.path.dirname(__file__), 'fixtures', 'nested_file2.json')
    with open(os.path.join(os.path.dirname(__file__), 'fixtures', 'test_result_nested_json.txt')) as result:
        test_result = ''.join(result.readlines())
    assert generate_diff(file1, file2) == test_result
