import json

from gendiff.compare_data import CHANGED, ADDED, REMOVED, NESTED


ADDED_TEMPLATE = 'Property \'{0}\' was added with value: {1}'
REMOVED_TEMPLATE = 'Property \'{0}\' was removed'
CHANGED_TEMPLATE = 'Property \'{0}\' was updated. From {1} to {2}'

COMPLEX_VALUE = '[complex value]'


def convert_to_plain(data, name=''):
    result = []

    for key, val in data.items():
        path = f'{name}.{key}'.lstrip('.')
        status = val.get('type')
        value = val.get('value')
        children = val.get('children')

        if status == ADDED:
            if isinstance(value, dict):
                value = COMPLEX_VALUE
            else:
                value = make_str(value)
            result.append(ADDED_TEMPLATE.format(path, value))

        elif status == REMOVED:
            result.append(REMOVED_TEMPLATE.format(path))

        elif status == CHANGED:
            if isinstance(value.get('old_type'), dict):
                old = COMPLEX_VALUE
                new = make_str(value.get('new_type'))
            elif isinstance(value.get('new_type'), dict):
                old = make_str(value.get('old_type'))
                new = COMPLEX_VALUE
            else:
                old = make_str(value.get('old_type'))
                new = make_str(value.get('new_type'))
            result.append(CHANGED_TEMPLATE.format(path, old, new))

        elif status == NESTED:
            if isinstance(children, dict):
                result.append(convert_to_plain(children, path))

    return '\n'.join(result)


def make_str(element):
    if isinstance(element, str):
        return f'\'{element}\''
    else:
        return json.dumps(element)
