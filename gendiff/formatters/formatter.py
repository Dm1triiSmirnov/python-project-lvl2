from .stylish import convert_to_stylish
from .json import convert_to_json
from .plain import convert_to_plain

STYLISH = 'stylish'
PLAIN = 'plain'
JSON = 'json'


accepted_formats = {STYLISH: convert_to_stylish,
                    JSON: convert_to_json,
                    PLAIN: convert_to_plain}


def formatter(data, format_name):
    return accepted_formats[format_name](data)
