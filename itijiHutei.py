# coding=utf-8
from Euclid import *
from equation import *

class itijiHutei(Euclid):

    def __init__(self):
        super(itijiHutei, self).__init__()
        self.inputNumC = -1
        self.resultList = []
        self.numAminus

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
                eq.setEquBase(remList[i], [[aList[i], 1], [bList[i], -mulList[i]]])
            else:
                eq.setEquAdd(remList[i], [[aList[i], 1], [bList[i], -mulList[i]]])
                # 2つの式を結合
                eq.margeEqu()
        # 計算結果を表示用のListに格納
        self.resultList = eq.getEquBase()
