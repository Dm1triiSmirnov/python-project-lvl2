import json

from gendiff.compare_data import UNCHANGED, CHANGED, ADDED, REMOVED

SPACE = ' '
TAB = SPACE * 4

symbols_dict = {UNCHANGED: TAB,
                ADDED: f'{SPACE * 2}+{SPACE}',
                REMOVED: f'{SPACE * 2}-{SPACE}'}


def convert_to_stylish(data, depth=0):
    result = ['{']
    depth += 1
    for key, val in data.items():
        indent = TAB * (depth - 1)
        status = val.get('type')
        value = val.get('value')
        children = val.get('children')

        if status == UNCHANGED or status == ADDED or status == REMOVED:
            result.append(adjust(indent, symbols_dict[status], key, make_str(value, depth + 1)))  # noqa E501

        elif status == CHANGED:
            result.append(adjust(indent, symbols_dict[REMOVED], key, make_str(value.get('old_type'), depth + 1)))  # noqa E501
            result.append(adjust(indent, symbols_dict[ADDED], key, make_str(value.get('new_type'), depth + 1)))  # noqa E501

        else:
            result.append(adjust(indent, symbols_dict[UNCHANGED], key, convert_to_stylish(children, depth)))  # noqa E501
    result.append(indent + '}')
    result = '\n'.join(result)
    return result


def adjust(indent, symbol, key, value):
    return f'{indent}{symbol}{key}: {value}'


def make_str(element, depth):
    if isinstance(element, str):
        return element
    elif isinstance(element, dict):
        result = ['{']
        indent = TAB * depth
        for key, value in element.items():
            result.append(f'{indent}{key}: {make_str(value, depth + 1)}')
        result.append(TAB * (depth - 1) + '}')
        result = '\n'.join(result)
        return result
    else:
        return json.dumps(element)
