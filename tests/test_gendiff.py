import os
from gendiff.generate_diff import generate_diff


def test_gediff_json():
    file1 = os.path.join(os.path.dirname(__file__), 'fixtures', 'file1.json')
    file2 = os.path.join(os.path.dirname(__file__), 'fixtures', 'file2.json')
    with open(os.path.join(os.path.dirname(__file__), 'fixtures', 'test_result_json.txt')) as result:
        json_test_result = result.readlines()
    assert generate_diff(file1, file2) == json_test_result

