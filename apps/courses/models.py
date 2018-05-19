from django.db import models

from datetime import datetime
from organization.models import CourseOrg
from organization.models import Teacher
# Create your models here.

# 课程信息表
class Course(models.Model):
    DEGREE_CHOICES = (
        ('cj', '初级'),
        ('zj', '中级'),
        ('gj', '高级')
    )
    name = models.CharField(max_length=60, verbose_name="课程名")
    desc = models.CharField(max_length=300, verbose_name="课程描述")

    # TextField允许我们不输入长度。可以输入到无限大。暂时定义为TextFiled，之后更新为富文本
    detail = models.TextField(verbose_name="课程详情")
    degree = models.CharField(choices=DEGREE_CHOICES, max_length=2)
    # 使用分钟作为后台记录（存储记录），后台转换
    learn_time = models.IntegerField(default=0, verbose_name="学习时长（分钟）")
    # 保存学习人数，点击开始学习才算
    students = models.IntegerField(default=0, verbose_name="学习人数")
    fav_nums = models.IntegerField(default=0, verbose_name="收藏人数")
    image = models.ImageField(
        upload_to="image/%Y/%m",
        verbose_name="封面图",
        max_length=100,
    )
    you_need_know = models.CharField(max_length=300, default=u"一颗勤学的心是本课程必要前提", verbose_name=u"课程须知")
    teacher_tell = models.CharField(max_length=300, default=u"按时交作业,不然叫家长", verbose_name=u"老师告诉你")

    # 保存点击量，点击页面就算
    click_num = models.IntegerField(default=0, verbose_name="点击量")
    tag = models.CharField(max_length=15, verbose_name=u"课程标签", default=u"")
    is_banner = models.BooleanField(default=False, verbose_name=u"是否轮播")
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    category = models.CharField(max_length=100, null=True, blank=True,verbose_name="课程类别")

    # 添加课程对应的机构外键
    course_org = models.ForeignKey(CourseOrg, verbose_name="所属机构", on_delete=models.CASCADE, null=True, blank = True)

    # 添加讲师对应的外键
    teacher = models.ForeignKey(Teacher, null=True, blank = True, on_delete=models.CASCADE)

    # 获取章节数和学习的用户，可以通过被置为外键的情况来计算
    def get_zj_nums(self):
        return self.lesson_set.all().count()

    def get_learn_user(self):
        return self.usercourse_set.all()[:5]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "课程"
        verbose_name_plural = verbose_name

# 每个课程的章节
class Lesson(models.Model):
    # 因为一个课程对应多个章节，所以在章节中设置为外键
    # 作为一个字段我们可以知道这个章节对应哪个课程
    course = models.ForeignKey(Course, verbose_name="课程", on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name="章节")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="上传时间")

    def __str__(self):
        return '《{0}》课程的章节 >> {1}'.format(self.course, self.name)

    class Meta:
        verbose_name = "章节"
        verbose_name_plural = verbose_name

# 每章节的视频
class Video(models.Model):
    # 一个章节中对应很多视频，在视频类中将章节设置成外键
    # 作为一个字段来存储可以让我们知道这个视频对应哪个章节
    lesson = models.ForeignKey(Lesson, verbose_name="章节", on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name="视频名")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="上传时间")

    url = models.CharField(max_length=200, default="http://127.0.0.1:8000/", verbose_name="访问地址")

    # 使用分钟做后台记录
    learn_time = models.IntegerField(default=0, verbose_name="学习时长（分钟数）")

    def __str__(self):
        return '{0}章节的视频>>{1}'.format(self.lesson, self.name)

    class Meta:
        verbose_name = "视频"
        verbose_name_plural = verbose_name

# 课程资源
class CourseResource(models.Model):
    # 因为一门课程对应很多资源，所以课程作为外键
    # 作为一个字段我们能知道这个资源对应哪个课程呢
    course = models.ForeignKey(Course, verbose_name="课程", on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name="资源名称")
    # 这里定义成文件类型的field，后台管理系统中会直接有上传的按钮。
    # FileField也是一个字符串类型，要指定最大长度。
    download = models.FileField(
        upload_to="course/resource/%Y/%m",
        verbose_name="资源文件",
        max_length=1000 # 资源设置100长度不够吧
    )
    add_time = models.DateTimeField(default=datetime.now, verbose_name='上传时间')

    class Meta:
        verbose_name = u"课程资源"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '《{0}》课程的资源: {1}'.format(self.course, self.name)