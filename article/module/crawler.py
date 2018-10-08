import article.module.nlp as nlp
from bs4 import BeautifulSoup
import requests

class Crawler:
    def __init__(self, press):
        self.press = press


    def scrap(self, url):
        if self.press == "chosun":
            return self.scrap_chosun(url)
        elif self.press == "hani":
            return self.scrap_hani(url)
        else:
            Exception("WrongPressParams: Press should be chosun or hani")

    def scrap_chosun(self, url):
        html = requests.get(url)
        html.encoding = 'utf-8'
        parser = BeautifulSoup(html.text, 'html.parser')
        articleBody = parser.find_all('div', {'class': 'par'})

        articleStringList = [i.text for i in articleBody]

        wordCount = nlp.morpAnalyze(articleStringList)
        title = parser.find('h1', {'id': 'news_title_text_id'}).text

        postInfo = {'press': self.press, 'title': title, 'url': url, 'word_count': wordCount[:5]}

        return postInfo

    def scrap_hani(self, url):
        pass