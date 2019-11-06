from django.conf.urls import re_path
from . import views


urlpatterns = [
    # work主页
    re_path(r'^$', views.index, name='index'),
    # 显示工作列表
    re_path(r'^Jobs/$', views.jobs, name='jobs'),
    # 显示单个详细工作及其计划
    re_path(r'^Jobs/(?P<job_id>\d+)/$', views.job, name='job'),
    # 显示单个详细计划
    re_path(r'^Projects/(?P<project_id>\d+)/$', views.project, name='project'),
]