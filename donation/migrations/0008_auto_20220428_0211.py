# Generated by Django 2.1.15 on 2022-04-28 02:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0007_post_category'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
    ]
