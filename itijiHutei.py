# coding=utf-8
from Euclid import *
from equation import *

class itijiHutei(Euclid):

    def __init__(self):
        super(itijiHutei, self).__init__()
        self.inputNumC = -1
        self.resultList = []
        # 入力がマイナスを含む場合はTrue
        self.numAminus = False
        self.numBminus = False

    # override
    def getInput(self):
        print('Ax + By = C')
        print'A =',
        # self.inputNumA = 1560
        self.inputNumA = int(raw_input())
        print'B =',
        # self.inputNumB = 1001
        self.inputNumB = int(raw_input())
        print'C =',
        # self.inputNumC = 13
        self.inputNumC = int(raw_input())
        self.checkNumAminus()
        self.checkNumBminus()

    def setNumA(self, _num):
        self.inputNumA = _num
        self.checkNumAminus()

    def setNumB(self, _num):
        self.inputNumB = _num
        self.checkNumBminus()

    def checkNumAminus(self):
        # 入力がマイナスを含む場合
        if self.inputNumA < 0:
            self.inputNumA = -self.inputNumA
            self.numAminus = True

    def checkNumBminus(self):
        if self.inputNumB < 0:
            self.inputNumB = -self.inputNumB
            self.numBminus = True


    @staticmethod
    def getListIndex(dimlist = []):
        returnList = []
        for singList in dimlist:
            returnList.append(singList[0])
        return returnList

    def showResult(self):
        i = 0
        for list1 in self.resultList:
            for list2 in list1:
               if i == 0:
                    print
               elif i % 2 == 0:
                   print '+' ,
               else:
                   print '*',
               print list2 ,
               i += 1
        print '=', self.inputNumC

    def doMath(self):
        aList = self.numAlist
        bList = self.numBlist
        remList = self.remList
        mulList = self.mulList

        listLength = len(self.numAlist)
        eq = equation()
        for i in range(0, listLength)[::-1]:
            print remList[i], ' = ', aList[i], ' * ', mulList[i], ' - ', bList[i]
            if i == listLength-1:
                # = 1 となる最初の式をセット
                eq.setEquBase(remList[i], [[aList[i], 1], [bList[i], -mulList[i]]])
            else:
                eq.setEquAdd(remList[i], [[aList[i], 1], [bList[i], -mulList[i]]])
                # 2つの式を結合
                eq.margeEqu()
        # 計算結果を表示用のListに格納
        self.resultList = eq.getEquBase()

        # 入力がマイナス値の場合に対応
        if self.numAminus:
            self.resultList[0][1] = self.resultList[0][1]
        if self.numBminus:
            self.resultList[1][1] = self.resultList[1][1]
