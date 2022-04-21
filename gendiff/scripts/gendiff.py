import argparse

from gendiff.gen_diff import generate_diff
from gendiff.formatters.formatter import STYLISH, JSON, PLAIN


def args_init():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format',
                        default=STYLISH,
                        choices=[STYLISH, PLAIN, JSON],
                        help='set format of output')
    args = parser.parse_args()
    return args


def main():
    args = args_init()
    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == '__main__':
    main()
