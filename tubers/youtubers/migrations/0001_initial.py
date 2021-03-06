# Generated by Django 4.0.2 on 2022-02-02 09:37

import ckeditor.fields
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Youtuber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('photo', models.ImageField(upload_to='media/ytubers/%y/%m/%d')),
                ('video_url', models.CharField(max_length=255)),
                ('description', ckeditor.fields.RichTextField()),
                ('city', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('height', models.IntegerField()),
                ('crew', models.CharField(choices=[('solo', 'solo'), ('small', 'small'), ('large', 'large')], max_length=255)),
                ('camera_type', models.CharField(choices=[('canon', 'canon'), ('red', 'red'), ('sony', 'sony'), ('fuji', 'fuji'), ('other', 'other')], max_length=255)),
                ('category', models.CharField(choices=[('code', 'code'), ('vlog', 'vlog'), ('comedy', 'comedy'), ('gaming', 'gaming'), ('cooking', 'cooking')], max_length=255)),
                ('subs_count', models.IntegerField()),
                ('is_featured', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 2, 15, 7, 41, 51097))),
            ],
        ),
    ]
