import argparse

from life import CLife
from test import TestAll

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
        TestAll()
    else:
        if args.inputfile != None:
            fin = open(args.inputfile, "r")
            Read = fin.readline
        else:
            Read = input

        n, m, k = Read().split()
        n = int(n)
        m = int(m)
        k = int(k)
        life = CLife(n, m)
        for i in range(n):
            l = list(Read())
            for j in range(m):
                life.Set(l[j], i, j)
            
        life.Play(k)

        if args.outputfile != None:
            fout = open(args.outputfile, "r")
            Write = fout.write
        else:
            Write = WriteInStd

        for i in range(n):
            for j in range(m):
                Write(life.Get(i, j))
            Write("\n")

        if args.inputfile != None:
            fin.close()
        if args.outputfile != None:
            fout.close()

Run()