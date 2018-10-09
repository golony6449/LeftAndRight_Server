from bs4 import BeautifulSoup
import requests

class SearchEngine:
    def __init__(self, press):
        self.press = press

    def do_search(self, keyword):
        if self.press == 'chosun':
            return self._search_in_chosun(keyword)

        elif self.press == 'hani':
            pass

        else:
            Exception("WrongPressParams: Press should be chosun or hani")

    def _search_in_chosun(self, keyword):
        url = 'http://search.chosun.com/search/total.search?pageconf=total&query={}'
        html = requests.get(url.format(keyword))
        html.encoding = 'utf-8'
        parser = BeautifulSoup(html.text, 'html.parser')

        # 관련 뉴스 검색 (지면기사, 커뮤니티 제외)
        article_list = parser.find_all('dl', {'class': 'search_news'})[1:6]
        article_list_parsed = self._parse_article_chosun(article_list)
        return article_list_parsed

    def _parse_article_chosun(self, article_list):
        result = []
        for article in article_list:
            block = article.find('dt')
            title = block.text.strip()
            addr = block.find('a').get('href')
            result.append((title, addr))
        return result