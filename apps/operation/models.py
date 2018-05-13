from datetime import datetime

from django.db import models
# 引入我们CourseComments需要的外键models
from users.models import UserProfile

from courses.models import Course


# Create your models here.

# 用户我要学习的表单
class UserAsk(models.Model):
    name = models.CharField(max_length=20, verbose_name="姓名")
    # 手机号码一定是11位吗
    mobile = models.CharField(max_length=11, verbose_name="手机")
    course_name = models.CharField(max_length=50, verbose_name="课程名")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "用户咨询"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '用户: {0} 手机号: {1}'.format(self.name, self.mobile)

# 用户对于课程评论
class CourseComments(models.Model):
    # 需要两个外键，1、用户  2、课程   将这两个外键import进来
    course = models.ForeignKey(Course, verbose_name="课程", on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, verbose_name="用户", on_delete=models.CASCADE)
    comments = models.CharField(max_length=250, verbose_name="评论")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="评论时间")

    class Meta:
        verbose_name = "课程评论"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '用户({0})对于《{1}》 评论 :'.format(self.user, self.course)

# 用户对于课程，机构，讲师的收藏
class UserFavorite(models.Model):
    # 会涉及到四个外键，用户，讲师，课程，机构，提前import
    TYPE_CHOICES = (
        ('1', '课程'),
        ('2', '课程机构'),
        ('3', '讲师')
    )
    user = models.ForeignKey(UserProfile, verbose_name="用户", on_delete=models.CASCADE)

    '''
    !!!!注意这里可能产生的bug，facv_id不知道干嘛的，而且根本没用到外键
    仅仅是用到了名字
    '''
    # 机智版，直接保存用户的id
    facv_id = models.IntegerField(default=0)
    # 表明收藏的是哪种类型
    fav_type = models.IntegerField(
        default=1,
        choices= TYPE_CHOICES,
        verbose_name="收藏类型"
    )
    add_time = models.DateTimeField(default=datetime.now, verbose_name="收藏时间")

    class Meta:
        verbose_name = "用户收藏"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '用户({0})收藏了{1} '.format(self.user, self.fav_type)

# 用户消息表
class UserMessage(models.Model):
    '''
    因为我们的消息有两种：发给全员或者某一个用户
    所以如果使用外键，每个消息要对应用户，很难实现全员消息

    机智版：0发给所有用户，其他数字为指定用户
    '''
    user = models.IntegerField(default=0, verbose_name="接收用户")
    message = models.CharField(max_length=500, verbose_name="消息内容")

    # 是否已读？
    has_read = models.BooleanField(default=False, verbose_name="是否已读")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "用户消息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '用户({0})接收了{1} '.format(self.user, self.message)

# 用户课程表
class UserCourse(models.Model):
    # 会涉及到两个外键，1、用户  2、课程
    course = models.ForeignKey(Course, verbose_name="课程", on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, verbose_name="用户", on_delete=models.CASCADE)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "用户课程"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '用户({0})学习了{1} '.format(self.user, self.course)