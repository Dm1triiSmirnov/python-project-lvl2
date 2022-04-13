import json

from gendiff.parse_data import UNCHANGED, CHANGED, ADDED, REMOVED

SPACE = ' '
TAB = SPACE * 4

symbols_dict = {
    UNCHANGED: TAB,
    ADDED: f'{SPACE * 2}+{SPACE}',
    REMOVED: f'{SPACE * 2}-{SPACE}'
    }


def convert_to_stylish(data, depth=0):
    result = ['{']
    depth += 1
    for key, value in data.items():
        status = value.get('status')
        name = value.get('value')
        children = value.get('children')
        indent = TAB * (depth - 1)
        if status == UNCHANGED:
            result.append(adjust_format(indent, symbols_dict[UNCHANGED], key, make_str(name, depth + 1)))

        elif status == ADDED:
            result.append(adjust_format(indent, symbols_dict[ADDED], key, make_str(name, depth + 1)))

        elif status == REMOVED:
            result.append(adjust_format(indent, symbols_dict[REMOVED], key, make_str(name, depth + 1)))

        elif status == CHANGED:
            result.append(adjust_format(indent, symbols_dict[REMOVED], key, make_str(name.get('old_status'), depth + 1)))
            result.append(adjust_format(indent, symbols_dict[ADDED], key, make_str(name.get('new_status'), depth + 1)))

        else:
            result.append(adjust_format(indent, symbols_dict[UNCHANGED], key, convert_to_stylish(children, depth)))
    result.append(indent + '}')
    result = '\n'.join(result)
    return result


def adjust_format(indent, symbol, key, value):
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
