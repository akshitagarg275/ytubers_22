from django.contrib import admin
from .models import Slider,Team
from django.utils.html import format_html
# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    def myphoto(self,object):
        return format_html('<img width="40" src={}/>'.format(object.photo.url))
    list_display = ('id','myphoto','fname','role','created_date')
    list_display_links=('id','fname')
    search_fields=('fname','role',)
    list_filter=('role',)



admin.site.register(Slider)
admin.site.register(Team,TeamAdmin)