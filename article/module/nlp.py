from konlpy.tag import Okt #,Twitter

def main():
    twitter = Okt()
    wordList = twitter.pos()

def morpAnalyze(inputStringList, count=None):
    twitter = Okt()
    wordDict = {}

    for item in inputStringList:
        wordList = twitter.pos(item, norm=True)

        for word in wordList:
            if word[1] == 'Noun':
                if not (word[0] in wordDict):
                    wordDict[word[0]] = 1
                else:
                    wordDict[word[0]] += 1

    if count == None:
        return wordDict

    keyList = [x for x in wordDict.keys()]
    valueList = []

    for key in keyList:
        valueList.append(wordDict[key])
        # print("({} : {})".format(key, wordDict[key]), end=" ")

    keyList, valueList = sortDict(keyList, valueList)

    # 슬라이싱
    resultDict = {}
    for idx in range(count):
        resultDict[keyList[idx]] = valueList[idx]
    return resultDict

    # test code
    # for key in keyList:
    #     print("( {} : {} )".format(key, wordDict[key]), end=" ")
    # print(end="\n\n")

def sortDict(keys, values):
    listLength = len(keys)
    for idxA in range(listLength):
        for idxB in range(listLength):
            if values[idxA] > values[idxB]:
                keys[idxA], keys[idxB] = keys[idxB], keys[idxA]
                values[idxA], values[idxB] = values[idxB], values[idxA]
    return keys, values

if __name__ == '__main__':
    main()