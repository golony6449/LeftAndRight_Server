import requests
from bs4 import BeautifulSoup


class Rss:
    def __init__(self):
        self.chosun = 'http://myhome.chosun.com/rss/www_section_rss.xml'    # 주요뉴스
        self.hani = 'http://www.hani.co.kr/rss/'                            # 전체기사
        # TODO: 한겨레는 rss의 item 태그 하위의 title 태그
        # TODO: 조선일보도 동일

    def scrap(self):
        # 한겨레 RSS 서비스 http://www.hani.co.kr/arti/RSS/list1.html
        # 조선일보 RSS 서비스 http://rssplus.chosun.com/

        html = requests.get(self.chosun)
        # html = requests.get(self.hani)
        parser = BeautifulSoup(html.text, 'lxml-xml')
        articleList = parser.find_all('item')
        for item in articleList:
            print(item.find('title').text)
            self.parserForChosun(item.find('link').text)
            # print(item.text)

        # print(parser)

    def parserForChosun(self, url):
        html = requests.get(url)
        html.encoding = 'utf-8'
        parser = BeautifulSoup(html.text, 'html.parser')
        articleBody = parser.find_all('div', {'class': 'par'})
        for item in articleBody:
            print(item.text)
            # print(item.text.encode('iso-8859-1').decode('utf-8'))