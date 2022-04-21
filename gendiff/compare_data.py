UNCHANGED = 'unchanged'
CHANGED = 'changed'
ADDED = 'added'
REMOVED = 'removed'
NESTED = 'nested'


def get_diff(data1, data2):
    result = dict()
    all_keys = sorted(data1.keys() | data2.keys())

    for key in all_keys:
        if key not in data2:
            result[key] = {
                'type': REMOVED,
                'value': data1[key],
                'children': None
            }
        elif key not in data1:
            result[key] = {
                'type': ADDED,
                'value': data2[key],
                'children': None
            }
        elif data1[key] == data2[key]:
            result[key] = {
                'type': UNCHANGED,
                'value': data1[key],
                'children': None
            }
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            result[key] = {
                'type': NESTED,
                'value': None,
                'children': get_diff(data1[key], data2[key])
            }
        else:
            result[key] = {
                'type': CHANGED,
                'value': {
                    'old_type': data1[key],
                    'new_type': data2[key]
                },
                'children': None
            }

    return result
