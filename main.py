import argparse
import sys

from life import Life
from test import Test


def get_parser_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--inputfile', action='store')
    parser.add_argument('--outputfile', action='store')
    parser.add_argument('--runtests', action='store_true')
    return parser.parse_args()


def run():
    args = get_parser_args()

    if args.runtests:
        Test.run()
    else:
        if args.inputfile is not None:
            sys.stdin = open(args.inputfile, "r")

        height, width, iterations = map(int, input().split())
        life = Life(height, width)
        for i in range(height):
            l = list(input())
            for j in range(width):
                life.set(l[j], i, j)
            
        life.play(iterations)

        if args.outputfile is not None:
            sys.stdout = open(args.outputfile, "w")

        for i in range(height):
            for j in range(width):
                print(life.get(i, j), end='')
            print()


if __name__ == "__main__":
    run()
