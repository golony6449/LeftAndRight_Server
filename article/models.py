from django.db import models

# Create your models here.
class press(models.Model):
    name = models.CharField(max_length=20, primary_key=True)
    url = models.CharField(max_length=30)
    is_left = models.BooleanField()

# TODO: Implement After User auth part
# class log(models.Model):
#     press_name = models.ForeignKey(press, on_delete=models.CASCADE)
#     user_name = model.
#     hits_count = models.IntegerField(default=0)

class recentPost(models.Model):
    index = models.AutoField(primary_key=True)
    name = models.ForeignKey('press', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now=True)
    keyword1 = models.CharField(max_length=20)
    keyword2 = models.CharField(max_length=20)
    keyword3 = models.CharField(max_length=20)
    keyword4 = models.CharField(max_length=20)
    keyword5 = models.CharField(max_length=20)