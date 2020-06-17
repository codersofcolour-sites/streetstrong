# Generated by Django 3.0.7 on 2020-06-17 18:49

from django.db import migrations
import streams.blocks
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('flex', '0002_flexpage_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flexpage',
            name='body',
            field=wagtail.core.fields.StreamField([('title_and_text', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add your title', required=True)), ('text', wagtail.core.blocks.TextBlock(held_text='Add additional text', required=True))])), ('full_richtext', streams.blocks.RichtextBlock()), ('simple_richtext', streams.blocks.SimpleRichtextBlock())], blank=True, null=True),
        ),
    ]
