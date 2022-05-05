import json
import yaml


def parse(text, format):
    if format == 'json':
        parsed_data = json.loads(text)
    elif format == 'yml' or format == 'yaml':
        parsed_data = yaml.safe_load(text)
    return parsed_data
