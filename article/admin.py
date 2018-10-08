from django.contrib import admin
from .models import press, recentPost

# Register your models here.
class PressAdmin(admin.ModelAdmin):
    fields = ['name', 'url', 'is_left']

class RecentPostAdmin(admin.ModelAdmin):
    fields = ['name', 'title', 'url',
              'keyword1', 'keyword2', 'keyword3', 'keyword4', 'keyword5']

admin.site.register(press, PressAdmin)
admin.site.register(recentPost, RecentPostAdmin)