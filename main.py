import argparse
import sys

from life import CLife
from test import CTest

def GetParserArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument('--inputfile', action='store')
    parser.add_argument('--outputfile', action='store')
    parser.add_argument('--runtests', action='store_true')
    return parser.parse_args()

def WriteInStd(arg):
    print(arg, end='')

def Run():
    args = GetParserArgs()

    if args.runtests:
        CTest.Run()
    else:
        if args.inputfile != None:
            sys.stdin = open(args.inputfile, "r")

        height, width, iterations = input().split()
        height = int(height)
        width = int(width)
        iterations = int(iterations)
        life = CLife(height, width)
        for i in range(height):
            l = list(input())
            for j in range(width):
                life.Set(l[j], i, j)
            
        life.Play(iterations)

        if args.outputfile != None:
            sys.stdout = open(args.outputfile, "w")

        for i in range(height):
            for j in range(width):
                print(life.Get(i, j), end='')
            print()


Run()