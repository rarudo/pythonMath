# coding=utf-8
from EuclidFrame import *


class Euclid(object):
    def __init__(self):
        super(Euclid, self).__init__()
        # コンソールから入力された値1
        self.inputNumA = -1
        # コンソールから入力された値1
        self.inputnumB = -1
        # 一時不定方程式用にaの値のlogをとっておく
        self.numAlist = []
        # 一時不定方程式用にbの値のlogをとっておく
        self.numBlist = []
        # 一時不定方程式用にあまりの値のlogをとっておく
        self.remList = []
        # 一時不定方程式用にかけ数のlogをとっておく
        self.mulList = []
        # 最大公約数の結果を格納
        self.result = -1

    # NumAlistにnumAの値のlogが入る
    def getNumAlist(self):
        return self.numalist

    # NumBlistにnumBの値のlogが入る
    def getNumBlist(self):
        return self.numblist

    # remListにrem(あまり)の値のlogが入る
    def getRemList(self):
        return self.remlist

    # inputNumA > inputNumB を常に維持するための処理
    def checkNum(self):
        # inputNumA > inputNumB を常に維持
        if self.inputNumB > self.inputNumA:
            tmp = self.inputNumA
            self.inputNumA = self.inputNumB
            self.inputNumB = tmp
        return

    # コンソールから得た値をフィールド変数へ格納するための処理
    def getInput(self):
        print('A と B の最大公約数を求める')
        print'A =',
        self.inputNumA = int(raw_input())
        print'B =',
        self.inputNumB = int(raw_input())
        self.checkNum()
        return

    @staticmethod
    def getRem(x, y):
        rem = x % y
        return rem

    @staticmethod
    def getMul(x, y):
        rem = x % y
        return (x - rem) / y

    # フィールド変数の中身を表示する
    def showLists(self):
        print self.numAlist
        print self.numBlist
        print self.remList
        print self.mulList
        return

    # 結果の表示処理
    def showResult(self):
        print self.inputNumA, 'と', self.inputNumB, 'の最大公約数は'
        print self.result
        return

    # ユークリッドから最大公約数を求める
    def getGcd(self):
        # numA = numB * mul + rem
        numA = self.inputNumA
        numB = self.inputNumB
        rem = -1
        if numA % numB == 0:
            # 100 と 10 であれば10が最大公約数
            rem = numB
        else:
            while numA % numB != 0:
                # 1次不定方程式用に計算過程をlistに追加
                self.numAlist.append(numA)
                self.numBlist.append(numB)
                self.mulList.append(self.getMul(numA, numB))
                rem = self.getRem(numA, numB)
                print numA, '=', numB, '+', rem
                numA = numB
                numB = rem
                # 1次不定方程式用に余りをリストに追加
                self.remList.append(rem)
        self.result = rem
        return rem
