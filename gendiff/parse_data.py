UNCHANGED = 'unchanged'
CHANGED = 'changed'
ADDED = 'added'
REMOVED = 'removed'
NESTED = 'nested'


def parse_data(data1, data2):
    result = dict()
    all_keys = sorted(data1.keys() | data2.keys())

    for key in all_keys:
        if key not in data2:
            result[key] = {
                'status': REMOVED,
                'value': data1[key],
                'children': None
            }
        elif key not in data1:
            result[key] = {
                'status': ADDED,
                'value': data2[key],
                'children': None
            }
        elif data1[key] == data2[key]:
            result[key] = {
                'status': UNCHANGED,
                'value': data1[key],
                'children': None
            }
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            result[key] = {
                'status': NESTED,
                'value': None,
                'children': parse_data(data1[key], data2[key])
            }
        else:
            result[key] = {
                'status': CHANGED,
                'value': {
                    'old_status': data1[key],
                    'new_status': data2[key]
                },
                'children': None
            }

    return result
