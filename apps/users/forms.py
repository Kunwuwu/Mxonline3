# encoding: utf-8
__author__ = 'jiakun2333'
__datetime__ = '2018/5/14 11:38'

# 引入forms表单
from django import forms

# 引入验证码field
from captcha.fields import CaptchaField

# 登录表单验证
class LoginForm(forms.Form):
    # 用户密码不能为空
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)

class RegisterForm(forms.Form):
    # 此处email与前端的name保持一致
    email = forms.EmailField(required=True)
    # 密码不能小于5位
    password = forms.CharField(required=True, min_length=5)
    # 应用验证码
    captcha = CaptchaField()

class ActiveForm(forms.Form):
    pass