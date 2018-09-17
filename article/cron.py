from django_cron import CronJobBase, Schedule
from article.models import recentPost, press
from article.module import rss

class crawlPost(CronJobBase):
    RUN_EVERY_MINS = 1
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'crawler'

    def do(self):
        print('cron"s work start!')
        chosun = rss.Rss('chosun')
        result = chosun.scrap(5)

        print('scrapping complete')

        for idx in range(len(result[0])):
            # TODO: FK 부분 참조 문제 발생
            pressObj = press.objects.get(name='chosun')
            query = recentPost(name=pressObj, title=result[idx][0])

            # TODO: 리펙토링
            temp = []
            for key in result[idx][1].keys():
                temp.append(key)

            query.keyword1 = temp[0]
            query.keyword2 = temp[1]
            query.keyword3 = temp[2]
            query.keyword4 = temp[3]
            query.keyword5 = temp[4]
            query.save()