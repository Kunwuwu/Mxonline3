# encoding: utf-8
__author__ = 'jiakun2333'
__datetime__ = '2018/5/14 11:38'

# 引入forms表单
from django import forms

# 登录表单验证
class LoginForm(forms.Form):
    # 用户密码不能为空
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)