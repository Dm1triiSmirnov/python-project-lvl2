import pytest
from gendiff.generate_diff import generate_diff


@pytest.fixture
def json_test_result():
    with open('fixtures/test_result_json.txt') as result:
        return result.readlines()


def test_gediff_json():
    file1 = 'tests/fixtures/file1.json'
    file2 = 'tests/fixtures/file2.json'
    assert generate_diff(file1, file2) == json_test_result

