from django.db import models

# Create your models here.
class press(models.Model):
    name = models.CharField(max_length=20)
    url = models.CharField(max_length=30)
    is_left = models.BooleanField()

# TODO: Implement After User auth part
# class log(models.Model):
#     press_name = models.ForeignKey(press, on_delete=models.CASCADE)
#     user_name = model.
#     hits_count = models.IntegerField(default=0)

class recentPost(models.Model):
    name = #TODO FK 설정
    title = models.CharField(max_length=100)
    keyword1 = models.CharField(max_length=20)
    keyword2 = models.CharField(max_length=20)
    keyword3 = models.CharField(max_length=20)