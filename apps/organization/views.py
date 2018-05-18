from django.shortcuts import render
from django.views.generic.base import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse

from .models import CourseOrg, CityDict, Teacher
from .forms import UserAskForm
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


# 添加我要学习
class AddUserAskView(View):
    # 处理表单提交当然post
    def post(self, request):
        userask_form = UserAskForm(request.POST)
        # 判断该form是否有效
        if userask_form.is_valid():
            # 注意这里model和form的区别
            # 它有model的属性
            # 当commit=true时进行真正保存
            user_ask = userask_form.save(commit=True)
            # 这样就不需要把一个一个字段取出来然后存到model的对象中之后save

            # 如果保存成功，返回json字段，后面content_type是告诉浏览器的
            return HttpResponse("{'status': 'success'}", content_type='application/json')
        else:
            # 如果保存失败，返回json字符串，并将forms的信息通过msg传送的前端
            return HttpResponse("{'status': 'success', 'msg':{0}}".format(userask_form.erros))


