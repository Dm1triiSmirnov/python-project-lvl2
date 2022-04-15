import json

from gendiff.parse_data import CHANGED, ADDED, REMOVED, NESTED


TEMPLATES = {
    ADDED: 'Property \'{0}\' was added with value: {1}',
    REMOVED: 'Property \'{0}\' was removed',
    CHANGED: 'Property \'{0}\' was updated. From {1} to {2}'
}


def convert_to_plain(data, name=''):
    result = []

    for key, val in data.items():
        status = val.get('status')
        value = val.get('value')
        children = val.get('children')
        path = f'{name}.{key}'.lstrip('.')

        if status == ADDED:
            if isinstance(value, dict):
                value = '[complex value]'
            else:
                value = make_str(value)
            result.append(TEMPLATES[ADDED].format(path, value))

        elif status == REMOVED:
            result.append(TEMPLATES[REMOVED].format(path))

        elif status == CHANGED:
            if isinstance(value.get('old_status'), dict):
                old = '[complex value]'
                new = make_str(value.get('new_status'))
            elif isinstance(value.get('new_status'), dict):
                old = make_str(value.get('old_status'))
                new = '[complex value]'
            else:
                old = make_str(value.get('old_status'))
                new = make_str(value.get('new_status'))
            result.append(TEMPLATES[CHANGED].format(path, old, new))

        elif status == NESTED:
            if isinstance(children, dict):
                result.append(convert_to_plain(children, path))

    return '\n'.join(result)


def make_str(element):
    if isinstance(element, str):
        return f'\'{element}\''
    else:
        return json.dumps(element)
