# Generated by Django 2.2.3 on 2019-07-09 15:32

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wagtailforms', '0003_capitalizeverbose'),
        ('home', '0006_sermonsbyscripture'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Profile',
            new_name='ProfilePage',
        ),
        migrations.RenameModel(
            old_name='SermonsByNumber',
            new_name='SermonsByNumberPage',
        ),
        migrations.RenameModel(
            old_name='SermonsByScripture',
            new_name='SermonsByScripturePage',
        ),
    ]
