# Generated by Django 3.0.6 on 2020-06-03 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_auto_20200602_2303'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='link',
            field=models.CharField(default='Not Available', max_length=200),
            preserve_default=False,
        ),
    ]