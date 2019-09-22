# Generated by Django 2.2.3 on 2019-09-21 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_remove_genesis_sermon_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exodus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sermon_scripture', models.TextField(default='설교 본문')),
                ('sermon_title', models.TextField(default='설교 제목')),
                ('sermon_link', models.URLField(default='https://leeyongkyu.s3-us-west-1.amazonaws.com/')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
