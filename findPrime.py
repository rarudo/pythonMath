# coding=utf-8
class findPrime():

    def __init__(self):
        # 10^N桁までマッピングするか
        self.maxMapping = 10 ** 4
        self.mapping = []
        self.primeList = []
        # N番目の素数を探す
        self.numN = -1

    def initMapping(self):
        for i in xrange(2, self.maxMapping):
            self.mapping.append(i)

    # 0 ~ 10000 までに求めたい素数がない場合
    # 10000 ~ 20000 までのリストを作る
    def extendMapping(self):
        preMax = self.maxMapping
        nexMax = self.maxMapping * 2
        for i in xrange(preMax, nexMax):
            self.mapping.append(i)
        self.maxMapping = nexMax

    def getInput(self):
        print 'N番目の素数を求める'
        print 'N = ',
        self.numN = int(raw_input())

    def showResult(self):
        print self.numN, '番目の素数は',self.primeList[self.numN-1]

    # 素数の倍数をmapping から削除
    def removePrime(self):
        _mappingList = self.mapping
        removeNum = self.primeList[-1]
        for pl in _mappingList:
            if pl % removeNum == 0:
                removeKey = self.mapping.index(pl)
                del(self.mapping[removeKey])

    # 素数のlistに含まれている倍数をmapping から一括削除
    def removePrimeAll(self):
        _mappingList = self.mapping
        for rm in self.primeList:
            for pl in _mappingList:
                if pl % rm == 0:
                    removeKey = self.mapping.index(pl)
                    del(self.mapping[removeKey])

    def getPrime(self):
        while len(self.mapping) > 0:
            self.primeList.append(self.mapping[0])
            self.removePrime()
        print self.primeList
        if self.numN > len(self.primeList):
            self.extendMapping()
            self.removePrimeAll()
            self.getPrime()
        else:
            return self.primeList

    # 総当りで割っていく方法
    def getPrime2(self):
        self.primeList = []
        for i in range(2, self.maxMapping):
            flag = 1
            for j in range(2, i):
                if i % j == 0:
                    flag = 0
                    break
            if flag == 1:
                self.primeList.append(i)
        print self.primeList
