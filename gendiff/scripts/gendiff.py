from gendiff.packages.args import args_init
from gendiff.packages.generate_diff import generate_diff


def main():
    args = args_init()
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)


if __name__=='__main__':
    main()
