from stylish import convert_to_stylish
from .json import convert_to_json
from plain import convert_to_plain


accepted_formats = {
    'stylish': convert_to_stylish,
    'json': convert_to_json,
    'plain': convert_to_plain
}

def formatter(data, format):
    try:
        accepted_formats[format](data)
    except KeyError:
        print('Selected format not supported')