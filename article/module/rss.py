import requests
from bs4 import BeautifulSoup
import nlp


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

    def scrap(self):
        # 한겨레 RSS 서비스 http://www.hani.co.kr/arti/RSS/list1.html
        # 조선일보 RSS 서비스 http://rssplus.chosun.com/

        html = requests.get(self.target)
        parser = BeautifulSoup(html.text, 'lxml-xml')
        articleList = parser.find_all('item')
        for item in articleList:
            print(item.find('title').text)

            if self.press is 'chosun':
                self.parserForChosun(item.find('link').text)
            elif self.press is 'hani':
                self.parserForHani(item.find('link').text)
            else:
                raise Exception('WrongPressName')


    def parserForChosun(self, url):
        html = requests.get(url)
        html.encoding = 'utf-8'
        parser = BeautifulSoup(html.text, 'html.parser')
        articleBody = parser.find_all('div', {'class': 'par'})

        articleStringList = [i.text for i in articleBody]

        nlp.morpAnalyze(articleStringList)


    def parserForHani(selfself, url):
        pass