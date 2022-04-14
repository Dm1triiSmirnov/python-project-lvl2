import json

from gendiff.parse_data import UNCHANGED, CHANGED, ADDED, REMOVED, NESTED


TEMPLATES = {
    ADDED: 'Property \'{name}\' was added with value: {value}',
    REMOVED: 'Property \'{name}\' was removed',
    CHANGED: 'Property \'{name}\' was updated. From {old} to {new}'
}

def convert_to_plain(data, name=[]):
    result = []

    for key, val in data.items():
        status = val.get('status')
        value = val.get('value')
        children = val.get('children')
        name.append('.' + key)

        if status == ADDED:
            if isinstance(value, dict):
                value = '[complex value]'
            result.append(TEMPLATES[ADDED].format(''.join(name), value))

        elif status == REMOVED:
            result.append(TEMPLATES[REMOVED].format(''.join(name)))

        elif status == CHANGED:
            if isinstance(value.get('old_value'), dict):
                old = '[complex value]'
                new = value.get('new_value')
            if isinstance(value.get('new_value'), dict):
                old = value.get('old_value')
                new = '[complex value]'
            else:
                pass
            result.append(TEMPLATES[CHANGED].format(''.join(name), old, new))

        elif status == NESTED:
            if isinstance(children, dict):
                result.append(convert_to_plain(children, name))

    return '\n'.join(result)


# def make_str(element):
#     if isinstance(element, str):
#         return element
#     else:
#         return json.dumps(element)


