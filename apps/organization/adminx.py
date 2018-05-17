# encoding: utf-8
__author__ = 'jiakun2333'
__datetime__ = '2018/5/13 13:38'

from .models import *     # 直接全部import了
import xadmin

# 机构所属城市名后台管理器
class CityDictAdmin(object):
    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc', 'add_time']

# 机构课程信息管理器
class CourseOrgAdmin(object):
    list_display = ['name', 'desc', 'category', 'click_nums', 'fav_nums', 'add_time']
    search_fields = ['name', 'desc', 'category', 'click_nums', 'fav_nums']
    list_filter = ['name', 'desc', 'category', 'click_nums', 'fav_nums', 'city__name', 'address', 'add_time']

class TeacherAdmin(object):
    list_display = ['name', 'work_years', 'work_company','org', 'work_position', 'fav_nums', 'points','add_time']
    search_fields = ['name', 'work_years', 'work_company','org', 'work_position']
    list_filter = ['name', 'work_years', 'work_company','org', 'work_position', 'fav_nums', 'points','add_time']

xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)