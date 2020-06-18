# Generated by Django 3.0.7 on 2020-06-17 18:54

from django.db import migrations
import streams.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('flex', '0003_auto_20200617_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flexpage',
            name='body',
            field=wagtail.core.fields.StreamField([('full_richtext', streams.blocks.RichtextBlock()), ('simple_richtext', streams.blocks.SimpleRichtextBlock())], blank=True, null=True),
        ),
    ]