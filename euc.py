# coding=utf-8
class euc(object):
    def __init__(self):
        # 初期化
        self.inputNumA = -1
        self.inputNumB = -1
        self.numAlist = []
        self.numBlist = []
        self.remList = []
        self.mulList = []
        self.result = -1 # 最大公約数の結果を格納

    def getNumAlist(self):
        return self.numAlist

    def getNumBlist(self):
        return self.numBlist

    def getRemList(self):
        return self.remList

    def checkNum(self):
        # inputNumA > inputNumB を常に維持
        if self.inputNumB > self.inputNumA:
            tmp = self.inputNumA
            self.inputNumA = self.inputNumB
            self.inputNumB = tmp

    def getInput(self):
        print('A と B の最大公約数を求める')
        print'A =',
        self.inputNumA = int(raw_input())
        print'B =',
        self.inputNumB = int(raw_input())
        self.checkNum()

    @staticmethod
    def getRem(x, y):
        rem = x % y
        return rem

    @staticmethod
    def getMul(x, y):
        rem = x % y
        return (x-rem)/y

    def showLists(self):
        print self.numAlist
        print self.numBlist
        print self.remList
        print self.mulList

    def showResult(self):
        print self.inputNumA, 'と', self.inputNumB, 'の最大公約数は'
        print self.result

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
                self.mulList.append(self.getMul(numA,numB))
                rem = self.getRem(numA, numB)
                print numA, '=', numB, '+', rem
                numA = numB
                numB = rem
                # 1次不定方程式用に余りをリストに追加
                self.remList.append(rem)
        self.result = rem
        return rem
