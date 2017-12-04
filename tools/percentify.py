#!/usr/bin/env python3
import sys
import math
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--sum', action='store_true', help='Use sum of all values instead of maximum value as reference')
    parser.add_argument('-f', '--field', default=0, type=int, help='Field to use. 0-based index.')
    parser.add_argument('-o', '--original', action='store_true', help='Output original lines instead of counts along with percentages')
    parser.add_argument('-t', '--table', action='store_true', help='Output rst table')
    parser.add_argument('-n', '--name', type=str, default='Content', help='Name of content column')
    parser.add_argument('input', type=argparse.FileType('r'), nargs='?', default=sys.stdin, help='Input file')
    args = parser.parse_args()

    lines = [ line.strip('\r\n') for line in args.input.readlines() ]
    nums = [ int(line.strip().split()[args.field]) for line in lines ]
    digits = int(math.log10(max(nums)))+1
    total = sum(nums) if args.sum else max(nums)

    maxlen = max(len(args.name), max(len(l) for l in lines))
    if args.table:
        digits = max(len('Count'), digits)
        strip_field = lambda arr, idx: arr[:idx] + arr[idx+1:]
        lines = [ ' '.join(strip_field(line.strip().split(), args.field)) for line in lines ]
        maxlen = max(len(args.name), max(len(l) for l in lines))
        print('='*maxlen, '='*digits, '=========')
        print(args.name.ljust(maxlen), 'Count'.ljust(digits), 'Frequency')
        print('='*maxlen, '='*digits, '=========')
    for line, num in zip(lines, nums):
        if args.table:
            print('{{:<{}}} {{:>{}}} {{:>{}.{}f}}%'.format(maxlen, digits, len('Frequency')-1, digits-3).format(line, num, num/total*100))
        elif args.original:
            print('{{:<{}}} {{:>{}.{}f}}%'.format(maxlen, digits+1, digits-3).format(line, num/total*100))
        else:
            print('{{:>{}}} {{:>{}.{}f}}%'.format(digits, digits+1, digits-3).format(num, num/total*100))
    if args.table:
        print('='*maxlen, '='*digits, '=========')

