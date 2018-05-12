from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserProfile(AbstractUser):
    # 自定义的性别选择规则
    GENDER_CHOICES = (
        ("male", "男"),
        ("female", "女")
    )
    # 昵称
    nick_name = models.CharField(max_length=50, verbose_name="昵称", default="")
    # 生日，可以为空
    birthday = models.DateField(verbose_name="生日", null=True, blank=True)
    # 性别，只能男女，默认为女
    gender = models.CharField(
        max_length=5,
        verbose_name="性别",
        choices = GENDER_CHOICES,
        default="female")
    # 地址
    address = models.CharField(max_length=100, verbose_name="地址", default="")
    # 电话
    mobile = models.CharField(max_length=15, null=True, blank=True)
    # 头像，默认使用default.png
    image = models.ImageField(
        upload_to="image/%Y/%m",
        default="image/default.png",
        max_length=100,
    )

    # meta信息，即后台栏目名
    class meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    # 返回对象名
    def __str__(self):
        return self.username
