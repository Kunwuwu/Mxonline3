from django.shortcuts import render
from django.views.generic.base import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from .models import CourseOrg, CityDict, Teacher
# Create your views here.

# 处理课程机构的view
class OrgView(View):
    def get(self, request):
        # 查找所有的课程机构
        all_orgs = CourseOrg.objects.all()
        # 取出所有的城市
        all_citys = CityDict.objects.all()
        # 统计课程机构数目
        org_nums = all_orgs.count()
        # 热门机构
        hot_orgs = all_orgs.order_by("-click_nums")[:3]
        # 对课程机构进行分页
        # 尝试获取get请求传递过来的page参数
        # 如果是不合法的配置参数默认返回第一页

        # 取出筛选出的城市，默认为空
        city_id = request.GET.get("city", "")
        # 取出筛选的类别，默认为空
        category = request.GET.get("ct", "")
        if category:
            all_orgs = all_orgs.filter(category=category)
        # 如果选择了某个城市，进行筛选
        if city_id:
            all_orgs = CourseOrg.objects.filter(city=city_id)

            # 进行排序
        sorts = request.GET.get('sort', "")
        if sorts:
            if sorts == "students":
                all_orgs = all_orgs.order_by("-students")
            else:
                all_orgs = all_orgs.order_by("-course_num")
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        # 表示从all中取出来5个，每页显示5个
        p = Paginator(all_orgs, 5, request=request)
        orgs = p.page(page)

        return render(request, "org-list.html", {
            "all_orgs": orgs,
            "all_citys": all_citys,
            "org_nums": org_nums,
            "city_id": city_id,
            "category": category,
            "hot_orgs": hot_orgs,
        })

