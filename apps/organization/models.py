from django.db import models

from datetime import datetime
# Create your models here.

# 城市字典
class CityDict(models.Model):
    name = models.CharField(max_length=20, verbose_name="城市")
    # 城市描述：备用不一定展示出来
    desc = models.CharField(max_length=200, verbose_name="城市描述")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "城市"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

# 课程机构
class CourseOrg(models.Model):
    # 机构类别
    ORG_CHOICES = (
        ("pxjg", "培训机构"),
        ("gx", "高校"),
        ("gr", "个人")
    )

    name = models.CharField(max_length=50, verbose_name="机构名称")
    # 机构描述
    desc = models.CharField(max_length=200, verbose_name="机构描述")
    # 机构类型
    category = models.CharField(max_length=20, choices=ORG_CHOICES, verbose_name="机构类别", default="gx")
    click_nums = models.IntegerField(default=0, verbose_name="点击数")
    fav_nums = models.IntegerField(default=0, verbose_name="收藏人数")
    # 当学生点击学习课程时，课程学生数+1
    students = models.IntegerField(default=0, verbose_name="学习人数")
    # 当发布课程时，机构的课程数+1
    course_num = models.IntegerField(default=0, verbose_name="课程数")
    image = models.ImageField(
        upload_to="org/%Y/%m",
        verbose_name="封面图",
        max_length=100)
    address = models.CharField(max_length=50, verbose_name="机构地址")
    # 一个城市可以有很多机构，通过设置city外键，变成课程机构的一个字段
    # 可以通过机构找到城市
    city = models.ForeignKey(CityDict, verbose_name="所在城市", on_delete=models.CASCADE)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "课程机构"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "课程机构: {0}".format(self.name)

# 讲师
class Teacher(models.Model):
    # 一个机构可以有很多的老师，所以我们在讲师表添加外键并把课程机构名称保存下来
    # 可以使我们通过讲师找到对应的机构
    org = models.ForeignKey(CourseOrg, verbose_name="所属机构", on_delete=models.CASCADE)
    name = models.CharField(max_length=50, verbose_name="教师名称")
    work_years = models.IntegerField(default=0, verbose_name="工作年限")
    work_company = models.CharField(max_length=50, verbose_name="就职公司")
    work_position =  models.CharField(max_length=50, verbose_name="公司职位")
    points = models.CharField(max_length=50, verbose_name="教学特点")
    click_nums = models.IntegerField(default=0, verbose_name="点击数")
    fav_nums = models.IntegerField(default=0, verbose_name="收藏人数")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "讲师"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "[{0}]的教师: {1}".format(self.org, self.name)
