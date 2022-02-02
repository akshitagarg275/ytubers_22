from django.db import models
import datetime
from ckeditor.fields import RichTextField
# Create your models here.

class Youtuber(models.Model):
    crew_choices=(
        ('solo','solo'),
        ('small','small'),
        ('large','large')
    )

    camera_choices=(
        ('canon','canon'),
        ('red','red'),
        ('sony','sony'),
        ('fuji','fuji'),
        ('other','other')
    )

    category_choices=(
        ('code','code'),
        ('vlog','vlog'),
        ('comedy','comedy'),
        ('gaming','gaming'),
        ('cooking','cooking')
    )

    name=models.CharField(max_length=255)
    price=models.IntegerField()
    photo=models.ImageField(upload_to='media/ytubers/%y/%m/%d')
    video_url=models.CharField(max_length=255)
    description=RichTextField()
    city=models.CharField(max_length=255)
    age=models.IntegerField()
    height=models.IntegerField()
    crew=models.CharField(max_length=255,choices=crew_choices)
    camera_type=models.CharField(max_length=255,choices=camera_choices)
    category=models.CharField(max_length=255,choices=category_choices)
    subs_count=models.IntegerField()
    is_featured=models.BooleanField(default=False)
    created_date=models.DateTimeField(default=datetime.datetime.now(),blank=True)