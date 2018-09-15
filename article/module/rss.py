import requests
from bs4 import BeautifulSoup
import article.module.nlp as nlp


class Rss:
    def __init__(self, press):
        chosun = 'http://myhome.chosun.com/rss/www_section_rss.xml'    # 주요뉴스
        hani = 'http://www.hani.co.kr/rss/'                            # 전체기사

        self.press = press
        if press is 'chosun':
            self.target = chosun
        elif press is 'hani':
            self.target = hani
        else:
            raise Exception('WrongPressName')

        # 한겨레는 rss의 item 태그 하위의 title 태그
        # 조선일보도 동일

    def scrap(self, count=None):
        # 한겨레 RSS 서비스 http://www.hani.co.kr/arti/RSS/list1.html
        # 조선일보 RSS 서비스 http://rssplus.chosun.com/

        html = requests.get(self.target)
        parser = BeautifulSoup(html.text, 'lxml-xml')
        articleList = parser.find_all('item')

        articleObjList = []
        for item in articleList:
            obj = []
            obj.append(item.find('title').text)

            # test Code
            # print(item.find('title').text)

            if self.press is 'chosun':
                obj.append(self.parserForChosun(item.find('link').text, None))
            elif self.press is 'hani':
                obj.append(self.parserForHani(item.find('link').text))
            else:
                raise Exception('WrongPressName')

            articleObjList.append(obj)

        return articleObjList


    def parserForChosun(self, url, count=None):
        html = requests.get(url)
        html.encoding = 'utf-8'
        parser = BeautifulSoup(html.text, 'html.parser')
        articleBody = parser.find_all('div', {'class': 'par'})

        articleStringList = [i.text for i in articleBody]

        wordDict = nlp.morpAnalyze(articleStringList, count)

        return wordDict


    def parserForHani(selfself, url):
        pass

    def pressName(self):
        return self.press