# Generated by Django 2.0.5 on 2018-05-13 01:57

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='课程名')),
                ('desc', models.CharField(max_length=300, verbose_name='课程描述')),
                ('detail', models.TextField(verbose_name='课程详情')),
                ('degree', models.CharField(choices=[('cj', '初级'), ('zj', '中级'), ('gj', '高级')], max_length=2)),
                ('learn_time', models.IntegerField(default=0, verbose_name='学习时长（分钟）')),
                ('students', models.IntegerField(default=0, verbose_name='学习人数')),
                ('fav_nums', models.IntegerField(default=0, verbose_name='收藏人数')),
                ('image', models.ImageField(upload_to='image/%Y/%m', verbose_name='封面图')),
                ('click_num', models.IntegerField(default=0, verbose_name='点击量')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '课程',
                'verbose_name_plural': '课程',
            },
        ),
        migrations.CreateModel(
            name='CourseResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='资源名称')),
                ('download', models.FileField(max_length=1000, upload_to='course/resource/%Y/%m', verbose_name='资源文件')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='上传时间')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course', verbose_name='课程')),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='章节')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='上传时间')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course', verbose_name='课程')),
            ],
            options={
                'verbose_name': '章节',
                'verbose_name_plural': '章节',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='视频名')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='上传时间')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Lesson', verbose_name='章节')),
            ],
            options={
                'verbose_name': '视频',
                'verbose_name_plural': '视频',
            },
        ),
    ]
