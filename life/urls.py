from django.conf.urls import re_path
from . import views


urlpatterns = [
    # life主页
    re_path(r'^$', views.index, name='index'),
    # 显示所有日志
    re_path(r'^Logs/$', views.logs, name='logs'),
    # 显示单个详细日志
    re_path(r'^Logs/(?P<log_id>\d+)/$', views.log, name='log'),
]