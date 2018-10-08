from konlpy.tag import Okt #,Twitter

def main():
    twitter = Okt()
    wordList = twitter.pos()

def morpAnalyze(inputStringList, returnDict=False):
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

    if returnDict is True:
        return wordDict

    # pre-processing for sort
    keyList = [x for x in wordDict.keys()]
    valueList = []

    for key in keyList:
        valueList.append(wordDict[key])
        # print("({} : {})".format(key, wordDict[key]), end=" ")

    # sort dict
    result = sortDict(keyList, valueList)

    return result

    # Legacy
    # # 슬라이싱
    # resultDict = {}
    # for idx in range(count):
    #     resultDict[keyList[idx]] = valueList[idx]
    # return resultDict

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
    result = []
    for idx in range(listLength):
        result.append((keys[idx], values[idx]))
    return result

if __name__ == '__main__':
    main()