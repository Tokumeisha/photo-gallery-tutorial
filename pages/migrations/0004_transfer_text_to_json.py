# Generated by Django 3.1.3 on 2020-11-30 21:09

from django.db import migrations

import json

def text_to_json(apps, schema_editor):
    Post = apps.get_model('pages', 'Post')

    for post in Post.objects.all():
        json_data = json.dumps({"main_content": post.main_content})
        post.new_main_content = json_data
        post.save()


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_post_new_main_content'),
    ]

    operations = [
        migrations.RunPython(text_to_json),
    ]