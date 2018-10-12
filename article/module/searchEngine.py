from bs4 import BeautifulSoup
import requests

class SearchEngine:
    def __init__(self, user_press):
        if user_press == 'chosun':
            self.press = 'hani'
        elif user_press == 'hani':
            self.press = 'chosun'
        else:
            Exception("SearchEngine: WrongPressParams")

    def do_search(self, keyword):
        if self.press == 'chosun':
            return self._search_in_chosun(keyword)

        elif self.press == 'hani':
            return self._search_in_hani(keyword)

        else:
            Exception("WrongPressParams: Press should be chosun or hani")

    def _search_in_chosun(self, keyword):
        url = 'http://m.chosun.com/svc/search.html?query={}'.format(keyword)
        html = requests.get(url)
        html.encoding = 'utf-8'
        parser = BeautifulSoup(html.text, 'html.parser')

        # 관련 뉴스 검색 (지면기사, 커뮤니티 제외)
        article_list = parser.find_all('div', {'class': 'list_inner'})[:5]
        article_list_parsed = self._parse_article_chosun(article_list)
        return article_list_parsed

    def _parse_article_chosun(self, article_list):
        result = []
        for article in article_list:
            block = article.find('div', {'class': 'tit'})
            title = block.find('a').text
            addr = block.find('a').get('href')
            date = block.find('span').text[:-4]
            result.append((title, addr, date))
        return result

    # Legacy Code
    # 조선일보의 데스크톱 사이트의 링크롤 반환하는 문제점 발견
    # Solution: 모바일 페이지용 크롤러 제작

    # def _search_in_chosun(self, keyword):
    #     url = 'http://search.chosun.com/search/total.search?pageconf=total&query={}'
    #     html = requests.get(url.format(keyword))
    #     html.encoding = 'utf-8'
    #     parser = BeautifulSoup(html.text, 'html.parser')
    #
    #     # 관련 뉴스 검색 (지면기사, 커뮤니티 제외)
    #     article_list = parser.find_all('dl', {'class': 'search_news'})[1:6]
    #     article_list_parsed = self._parse_article_chosun(article_list)
    #     return article_list_parsed
    #
    # def _parse_article_chosun(self, article_list):
    #     result = []
    #     for article in article_list:
    #         block = article.find('dt')
    #         title = block.text.strip()
    #         addr = block.find('a').get('href')
    #         result.append((title, addr))
    #     return result

    def _search_in_hani(self, keyword):
        url = 'http://search.hani.co.kr/Search?command=query&keyword={}&sort=s&period=year&media=news'.format(keyword)
        html = requests.get(url)
        html.encoding = 'utf-8'
        parser = BeautifulSoup(html.text, 'html.parser')

        article_list = parser.find('ul', {'class': 'search-result-list'}).find_all('li')
        article_list_parsed = self._parse_article_hani(article_list)
        return article_list_parsed

        # 뉴스 전체 목록 중 1페이지만 (15개 기사)
        # article_list = parser.find_all('li')
        # article_list_parsed = self._parse_article_hani(article_list)
        # return article_list_parsed

    def _parse_article_hani(self, article_list):
        result = []

        for article in article_list:
            block = article.find('dl')
            tag_a = block.find('dt').find('a')
            title = tag_a.text
            addr = 'http://m' + tag_a.get('href')[10:]
            date = block.find('dd', {'class': 'date'}).find('dd').text[:-6]
            print()

        # # Legacy Code
        # for article in article_list:
        #     block = article.find('div', {'class': 'text'})
        #     tag_a_list = block.find_all('a')
        #     title = tag_a_list[0].text
        #     addr = 'http://m' + tag_a_list[0].get('href')[10:]
        #     date = tag_a_list[1].text[:-6]

            # title = block.find('h4').text
            # addr = block.find('a').get('href')
            # date = block.find('div')

            result.append((title, addr, date))
        return result
