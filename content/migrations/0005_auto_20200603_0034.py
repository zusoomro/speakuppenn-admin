# Generated by Django 3.0.6 on 2020-06-03 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0004_match_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='link',
            field=models.URLField(),
        ),
    ]