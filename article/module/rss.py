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
        parser = BeautifulSoup(html.text, 'lxml-xml')
        articleList = parser.find_all('item')
        for item in articleList:
            print(item.find('title').text)
            print(item.text)

        # print(parser)