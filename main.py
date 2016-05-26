# coding=utf-8
from euc import *
from itijiHutei import *
from findPrime import *


def doEuc():
    c = euc()
    c.getInput()
    c.getGcd()
    c.showResult()


def doItiji():
    c = itijiHutei()
    c.getInput()
    c.getGcd()
    print 'ユークリッドの互除法　終了'
    c.doMath()
    c.showResult()


def doPrime():
    c = findPrime()
    c.getInput()
    c.initMapping()
    c.getPrime()
    c.showResult()


def main():
    print '1)ユークリッドの互除法'
    print '2)一時不定方程式'
    print '3)素数探索'
    print 'input number'
    mode = raw_input()
    if mode == '1':
        doEuc()
    elif mode == '2':
        doItiji()
    elif mode == '3':
        doPrime()
    else:
        main()

if __name__ == "__main__":
    main()
