# from rss import Rss
#
# module = Rss('chosun')
# module.scrap()

from crawler import Crawler

module = Crawler('chosun')
result = module.scrap('http://news.chosun.com/site/data/html_dir/2018/10/08/2018100802172.html')
print(result)