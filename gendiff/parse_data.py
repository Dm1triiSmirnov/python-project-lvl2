
ADDED = '+'
DELETED = '-'


def parse_data(data1, data2):
    result = []
    all_keys = data1.keys() | data2.keys()
    all_keys.sort()

    for key in all_keys:
        if key in data1 and key in data2:
            pass

        elif key not in data2:
            result.append(f'    {key}: {data1[key]}')

        elif key not in data1:
            result.append(f'    {key}: {data2[key]}')


