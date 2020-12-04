# Generated by Django 3.1.4 on 2020-12-03 21:59

from django.db import migrations, models
import django.db.models.deletion
import pages.models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_auto_20201130_2309'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=pages.models.upload_gallery_image)),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='pages.pet')),
            ],
        ),
    ]
