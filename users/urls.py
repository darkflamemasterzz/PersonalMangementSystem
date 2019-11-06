from django.conf.urls import re_path
from django.contrib.auth.views import LoginView
from .import views


urlpatterns = [
    # 登录页面
    re_path(r'^login/$', LoginView.as_view(), name='login'),
    # 注销页面
    re_path(r'^logout/$', views.logout_view, name='logout'),
    # 注册页面
    re_path(r'^register/$', views.register, name='register'),
]