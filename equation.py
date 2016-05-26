# coding=utf-8
class equation :
    def __init__(self):
        self.leftEquBase = -1
        self.rightEquBase = []
        self.rightEquBaseIndex = []
        self.rightEquBaseMul = []
        self.leftEquAdd = -1
        self.rightEquAdd = []
        self.rightEquAddIndex = []
        self.rightEquAddMul = []

    def preInit(self):
        self.rightEquAddIndex = []
        self.rightEquAddMul = []

    def resetBaseIndex(self):
        self.rightEquBaseIndex = []
        self.rightEquBaseMul = []
        for re in self.rightEquBase:
            self.rightEquBaseIndex.append(re[0])
            self.rightEquBaseMul.append(re[1])

    # leftEqu = rightEqu[0][0] * rightEqu[0][1]  + rightEqu[1][0] * rightEqu[1][1]
    # 例   13  =     91         *       1         +      26        *       -3
    def setEquBase(self, leftEqu, rightEqu=[]):
        self.leftEquBase = leftEqu
        self.rightEquBase = rightEqu
        for re in rightEqu:
            # rightEqu 2次元配列　を1次元配列2つに分解
            self.rightEquBaseIndex.append(re[0])
            self.rightEquBaseMul.append(re[1])

    def setEquAdd(self, leftEqu, rightEqu=[]):
        self.leftEquAdd = leftEqu
        self.rightEquAdd = rightEqu
        self.preInit()
        self.resetBaseIndex()
        for re in rightEqu:
            # rightEqu 2次元配列　を1次元配列2つに分解
            self.rightEquAddIndex.append(re[0])
            self.rightEquAddMul.append(re[1])

    def getEquBase(self):
        return self.rightEquBase

    # 2次元list から　1次元目の値が重複しているものを削除
    @staticmethod
    def removeDup(equationList = []):
        equIndex = []
        equMul = []
        returnList = []
        returnListIndex = []
        returnListMul = []
        for re in equationList:
            # equationList 2次元配列　を1次元配列2つに分解
            equIndex.append(re[0])
            equMul.append(re[1])
        i = 0
        for ei in equIndex:
            if ei not in returnListIndex:
                returnListIndex.append(ei)
                returnListMul.append(equMul[equIndex.index(ei)])
            else:
                mul = equMul[i]
                returnListMul[returnListIndex.index(ei)] += mul
            i += 1
        for j in range(len(returnListIndex)):
            returnList.append([returnListIndex[j], returnListMul[j]])
        return returnList

    # 2つの式を結合する
    # 13 = 91 - 26 * 3
    # 26 = 117 - 91 * 1
    # から
    # 13 = 117 * -3 + 91 * 4
    # を導く
    def margeEqu(self):
        for rebi in self.rightEquBaseIndex:
            if rebi == self.leftEquAdd:
                findKey = self.rightEquBaseIndex.index(rebi)
                findMul = self.rightEquBaseMul[findKey]
                del self.rightEquBase[findKey]
                for i in range(len(self.rightEquAddMul)):
                    self.rightEquAddMul[i] *= findMul
                for j in range(len(self.rightEquAddIndex)):
                    self.rightEquBase.append([self.rightEquAddIndex[j], self.rightEquAddMul[j]])
                self.rightEquBase = self.removeDup(self.rightEquBase)

    def showEqu(self):
        print self.leftEquBase
        print self.rightEquBase
        print self.rightEquBaseIndex
        print self.rightEquBaseMul
        print self.leftEquAdd
        print self.rightEquAdd
        print self.rightEquAddIndex
        print self.rightEquAddMul
