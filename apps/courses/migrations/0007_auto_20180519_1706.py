# Generated by Django 2.0.5 on 2018-05-19 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0005_teacher_image'),
        ('courses', '0006_course_is_banner'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='organization.Teacher'),
        ),
        migrations.AddField(
            model_name='course',
            name='teacher_tell',
            field=models.CharField(default='按时交作业,不然叫家长', max_length=300, verbose_name='老师告诉你'),
        ),
        migrations.AddField(
            model_name='course',
            name='you_need_know',
            field=models.CharField(default='一颗勤学的心是本课程必要前提', max_length=300, verbose_name='课程须知'),
        ),
        migrations.AddField(
            model_name='video',
            name='learn_time',
            field=models.IntegerField(default=0, verbose_name='学习时长（分钟数）'),
        ),
        migrations.AddField(
            model_name='video',
            name='url',
            field=models.CharField(default='http://127.0.0.1:8000/', max_length=200, verbose_name='访问地址'),
        ),
    ]
