import argparse


def calc(args):
    if args.operation == 'add':
        return args.x + args.y
    if args.operation == 'sub':
        return args.x - args.y
    if args.operation == 'mul':
        return args.x * args.y
    if args.operation == 'div':
        if args.y != 0:
            return args.x / args.y
        else:
            return 'Division by zero not possible'


def main():
    parser = argparse.ArgumentParser(description='Do simple math operation for two given numbers')
    parser.add_argument('--verbose', '-v', help='Increase output verbosity', action="store_true")
    parser.add_argument('-x', '--x', type=float, default=1.0,
                        help='What is the first number')
    parser.add_argument('-y', '--y', type=float, default=1.0,
                        help='What is the second number')
    parser.add_argument('operation', help='Which operation? add sub mul div',
                        choices=['add', 'sub', 'mul', 'div'])

    args = parser.parse_args()

    result = calc(args)
    if args.verbose:
        print(f"{args.x} {args.operation}ed {args.y} = {result}")
    else:
        print(result)


if __name__ == '__main__':
    main()
