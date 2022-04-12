import json

from gendiff.parse_data import UNCHANGED, CHANGED, ADDED, REMOVED

SPACE = ' '
TAB = SPACE * 4

symbols_dict = {
    UNCHANGED: TAB,
    ADDED: f'{SPACE * 2}+{SPACE}',
    REMOVED: f'{SPACE * 2}-{SPACE}'
    }


def convert_to_stylish(data):
    result = ['{']
    for key, value in data.items():
        status = value.get('status')
        name = value.get('value')
        children = value.get('children')

        if status == UNCHANGED:
            result.append(adjust_format(TAB, symbols_dict[UNCHANGED], key, make_str(name)))

        elif status == ADDED:
            result.append(adjust_format(TAB, symbols_dict[ADDED], key, make_str(name)))

        elif status == REMOVED:
            result.append(adjust_format(TAB, symbols_dict[REMOVED], key, make_str(name)))

        elif status == CHANGED:
            result.append(adjust_format(TAB, symbols_dict[REMOVED], key, make_str(name.get('old_status'))))
            result.append(adjust_format(TAB, symbols_dict[ADDED], key, make_str(name.get('new_status'))))

        else:
            result.append(adjust_format(TAB, symbols_dict[UNCHANGED], key, convert_to_stylish(children)))
    result.append('}')
    result = '\n'.join(result)
    return result


def adjust_format(indent, symbol, key, value):
    return f'{indent}{symbol}{key}: {value}'



def make_str(element):
    if isinstance(element, str):
        return element
    elif isinstance(element, dict):
        result = ['{']
        for key, value in element.items():
            result.append(f'{TAB}{key}: {make_str(value)}')
        result.append('}')
        result = '\n'.join(result)
        return result
    else:
        return json.dumps(element)



