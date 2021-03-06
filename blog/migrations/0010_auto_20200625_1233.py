# Generated by Django 3.0.7 on 2020-06-25 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0022_uploadedimage'),
        ('blog', '0009_auto_20200625_1218'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpage',
            name='image',
        ),
        migrations.AddField(
            model_name='blogpage',
            name='banner_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='blogpage',
            name='intro_image',
            field=models.ForeignKey(blank=True, help_text='Best size for this image will be 1400x400', null=True, on_delete=django.db.models.deletion.SET_NULL, to='wagtailimages.Image'),
        ),
    ]
