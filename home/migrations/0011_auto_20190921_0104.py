# Generated by Django 2.2.3 on 2019-09-21 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_sermonsbyscripturesubpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genesis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sermon_scripture', models.TextField(default='설교 본문')),
                ('sermon_title', models.TextField(default='설교 제목')),
                ('sermon_link', models.URLField(default='https://leeyongkyu.s3-us-west-1.amazonaws.com/')),
            ],
        ),
        migrations.RemoveField(
            model_name='sermonsbyscripturesubpage',
            name='scripture',
        ),
        migrations.RemoveField(
            model_name='sermonsbyscripturesubpage',
            name='sermon_link',
        ),
        migrations.RemoveField(
            model_name='sermonsbyscripturesubpage',
            name='sermon_title',
        ),
    ]