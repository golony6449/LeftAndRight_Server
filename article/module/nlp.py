from konlpy.tag import Okt #,Twitter
def main():
    twitter = Okt()
    wordList = twitter.pos()

def morpAnalyze(inputStringList):
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

    for key in wordDict.keys():
        print("({} : {})".format(key, wordDict[key]), end=" ")

    print()
    print()

if __name__ == '__main__':
    main()