# Generated by Django 2.0.5 on 2018-05-13 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20180512_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('male', '男'), ('female', '女')], default='female', max_length=6, verbose_name='性别'),
        ),
    ]
