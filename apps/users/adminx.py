# encoding: utf-8
__author__ = 'jiakun2333'
__datetime__ = '2018/5/13 12:03'
# 把全站的配置放在users\adminx.py中:

import xadmin
from xadmin import views
from xadmin.models import Log
from django.contrib.auth.models import Group, Permission

from courses.models import Course, Video, Lesson, CourseResource
from organization.models import CityDict, Teacher, CourseOrg
from operation.models import CourseComments, UserFavorite, UserAsk, UserProfile, UserMessage, UserCourse

from .models import *

# 创建admin的管理类，这里不再是继承admin，而是继承object
#@xadmin.site.register(EmailVerifyRecord)  # 不能用装饰器，会报错
class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['email', 'code', 'send_type']
    list_filter = ['code', 'email', 'send_type', 'send_time']

class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'add_time']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']


# 下面是xadmin的全局设置
# 主题
class BaseSettings(object):
    # 开启主题功能
    enable_themes = True
    user_bootswatch = True

# xadmin 全局配置参数设置
class GlobalSetting(object):
    site_title = "2333：慕课后台管理站"
    site_footer = "Jiakun's mooc"
    # 收起菜单
    menu_style = "accordion"

    def get_site_menu(self):
        return (
            {'title': '机构管理', 'menus': (
                {'title': '所在城市', 'url': self.get_model_url(CityDict, 'changelist')},
                {'title': '机构信息', 'url': self.get_model_url(CourseOrg, 'changelist')},
                {'title': '机构讲师', 'url': self.get_model_url(Teacher, 'changelist')},
            )},
            {'title': '课程管理', 'menus': (
                {'title': '课程信息', 'url': self.get_model_url(Course, 'changelist')},
                {'title': '章节信息', 'url': self.get_model_url(Lesson, 'changelist')},
                {'title': '视频信息', 'url': self.get_model_url(Video, 'changelist')},
                {'title': '课程资源', 'url': self.get_model_url(CourseResource, 'changelist')},
                {'title': '课程评论', 'url': self.get_model_url(CourseComments, 'changelist')},
            )},

            {'title': '用户管理', 'menus': (
                {'title': '用户信息', 'url': self.get_model_url(UserProfile, 'changelist')},
                {'title': '用户验证', 'url': self.get_model_url(EmailVerifyRecord, 'changelist')},
                {'title': '用户课程', 'url': self.get_model_url(UserCourse, 'changelist')},
                {'title': '用户收藏', 'url': self.get_model_url(UserFavorite, 'changelist')},
                {'title': '用户消息', 'url': self.get_model_url(UserMessage, 'changelist')},
            )},


            {'title': '系统管理', 'menus': (
                {'title': '用户咨询', 'url': self.get_model_url(UserAsk, 'changelist')},
                {'title': '首页轮播', 'url': self.get_model_url(Banner, 'changelist')},
                {'title': '用户分组', 'url': self.get_model_url(Group, 'changelist')},
                {'title': '用户权限', 'url': self.get_model_url(Permission, 'changelist')},
                {'title': '日志记录', 'url': self.get_model_url(Log, 'changelist')},
            )},
        )



xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
# 将xadmin全局设定与view进行绑定注册
xadmin.site.register(views.BaseAdminView, BaseSettings)
# 将头部与脚部信息进行注册
xadmin.site.register(views.CommAdminView, GlobalSetting)