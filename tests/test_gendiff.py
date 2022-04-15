import os

from gendiff.generate_diff import generate_diff


def test_gendiff_flat_json():
    file1 = os.path.join(os.path.dirname(__file__), 'fixtures', 'flat_file1.json')
    file2 = os.path.join(os.path.dirname(__file__), 'fixtures', 'flat_file2.json')
    with open(os.path.join(os.path.dirname(__file__), 'test_results', 'test_result_flat.txt')) as result:
        test_result = ''.join(result.readlines())
    assert generate_diff(file1, file2) == test_result


def test_gendiff_flat_yaml():
    file1 = os.path.join(os.path.dirname(__file__), 'fixtures', 'flat_file1.yaml')
    file2 = os.path.join(os.path.dirname(__file__), 'fixtures', 'flat_file2.yaml')
    with open(os.path.join(os.path.dirname(__file__), 'test_results', 'test_result_flat.txt')) as result:
        test_result = ''.join(result.readlines())
    assert generate_diff(file1, file2) == test_result


def test_gendiff_json_stylish():
    file1 = os.path.join(os.path.dirname(__file__), 'fixtures', 'nested_file1.json')
    file2 = os.path.join(os.path.dirname(__file__), 'fixtures', 'nested_file2.json')
    with open(os.path.join(os.path.dirname(__file__), 'test_results', 'test_result_nested_stylish.txt')) as result:
        test_result = ''.join(result.readlines())
    assert generate_diff(file1, file2) == test_result


def test_gendiff_yaml_stylish():
    file1 = os.path.join(os.path.dirname(__file__), 'fixtures', 'nested_file1.yaml')
    file2 = os.path.join(os.path.dirname(__file__), 'fixtures', 'nested_file2.yaml')
    with open(os.path.join(os.path.dirname(__file__), 'test_results', 'test_result_nested_stylish.txt')) as result:
        test_result = ''.join(result.readlines())
    assert generate_diff(file1, file2) == test_result


def test_gendiff_json_plain():
    file1 = os.path.join(os.path.dirname(__file__), 'fixtures', 'nested_file1.json')
    file2 = os.path.join(os.path.dirname(__file__), 'fixtures', 'nested_file2.json')
    with open(os.path.join(os.path.dirname(__file__), 'test_results', 'test_result_nested_plain.txt')) as result:
        test_result = ''.join(result.readlines())
    assert generate_diff(file1, file2, 'plain') == test_result


def test_gendiff_yaml_plain():
    file1 = os.path.join(os.path.dirname(__file__), 'fixtures', 'nested_file1.yaml')
    file2 = os.path.join(os.path.dirname(__file__), 'fixtures', 'nested_file2.yaml')
    with open(os.path.join(os.path.dirname(__file__), 'test_results', 'test_result_nested_plain.txt')) as result:
        test_result = ''.join(result.readlines())
    assert generate_diff(file1, file2, 'plain') == test_result