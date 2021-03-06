# Generated by Django 2.2.3 on 2019-07-08 21:16

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('home', '0003_auto_20190708_2111'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='paragraph2',
            field=wagtail.core.fields.RichTextField(default='故 이용규 목사 유작 ( 遺作 ) 성경강해 설교집 총 42권'),
        ),
    ]
