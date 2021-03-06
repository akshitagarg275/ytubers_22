from django.contrib import admin
from .models import Youtuber
from django.utils.html import format_html
# Register your models here.

class YoutuberAdmin(admin.ModelAdmin):
    def myphoto(self,object):
        return format_html('<img width="40" src={}/>'.format(object.photo.url))
    list_display=('id','name','myphoto','subs_count','is_featured')
    search_fields=('name','camera_type')
    list_filter=('city','category')
    list_display_links=('id','name')
    list_editable=('is_featured',)

admin.site.register(Youtuber,YoutuberAdmin)