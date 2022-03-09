ADDED = '+'
DELETED = '-'


def parse_data(data1, data2):
    result = ['{']
    all_keys = sorted(data1.keys() | data2.keys())

    for key in all_keys:
        if key in data1 and key in data2:
            if data1[key] == data2[key]:
                result.append(f'    {key}: {data1[key]}')
            else:
                result.append(f'  {DELETED} {key}: {data1[key]}')
                result.append(f'  {ADDED} {key}: {data2[key]}')

        elif key not in data2:
            result.append(f'  {DELETED} {key}: {data1[key]}')

        elif key not in data1:
            result.append(f'  {ADDED} {key}: {data2[key]}')

    result = map(lambda el: el + '\n', result)
    result = list(map(str.lower, result))
    result.append('}')

    return result
