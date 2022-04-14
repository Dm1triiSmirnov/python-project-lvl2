from gendiff.parse_data import UNCHANGED, CHANGED, ADDED, REMOVED, NESTED


def convert_to_plain(data):
    result = []

    for key, value in data.items():
        status = value.get('status')
        val = value.get('value')
        children = value.get('children')

        if status == ADDED:
            pass

        elif status == REMOVED:
            pass

        elif status == CHANGED:
            pass

        elif status == NESTED:
            pass



