# encoding: utf-8
__author__ = 'jiakun2333'
__datetime__ = '2018/5/13 13:15'
# Course的admin管理器

from .models import *     # 直接全部import了
import xadmin

class CourseAdmin(object):
    list_display = ['name', 'desc', 'course_org', 'degree', 'learn_time', 'students']
    search_fields = ['name', 'desc', 'detail', 'degree', 'students']
    list_filter = ['name', 'desc', 'detail', 'degree', 'learn_time', 'students']

class LessonAdmin(object):
    list_display = ['name', 'course', 'add_time']
    search_fields = ['name', 'course']
    # __name代表使用外键中name字段，过滤器用，下同
    list_filter = ['course__name', 'name', 'add_time']

class VideoAdmin(object):
    list_display = ['name', 'lesson', 'add_time']
    search_fields = ['name', 'lesson']
    list_filter = ['name', 'lesson__name', 'add_time']

class CourseResourceAdmin(object):
    list_display = ['name', 'course', 'download', 'add_time']
    search_fields = ['name', 'course', 'download']
    list_filter = ['name', 'course__name', 'download', 'add_time']


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)

