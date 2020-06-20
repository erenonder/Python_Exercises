import argparse


def main():
    parser = argparse.ArgumentParser(description='Calculates given power of given base')
    parser.add_argument('-v', '--verbosity', action='store_true')
    parser.add_argument('base', type=int, help='Base number')
    parser.add_argument('power', type=int, help='Power number')
    args = parser.parse_args()
    if args.verbosity:
        print(f"{args.power}th power of {args.base} is {args.base**args.power}")
    else:
        print(args.base**args.power)


if __name__ == '__main__':
    main()
