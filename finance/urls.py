"""定义finance的url模式"""

from django.conf.urls import re_path
from . import views

urlpatterns = [
    # finance主页
    re_path(r'^$', views.index, name='index'),
    # 显示所有收入和支出记录
    re_path(r'^Record/$', views.record, name='record'),
    # 显示详细收入记录
    re_path(r'^Record/Income/(?P<income_id>\d+)/$', views.income, name='income'),
    # 显示详细支出记录
    re_path(r'^Record/Expense/(?P<expense_id>\d+)/$', views.expense, name='expense'),
    # 用于添加新收入记录的网页
    re_path(r'^new_income/$', views.new_income, name='new_income'),
    # 用于添加新支出记录的网页
    re_path(r'^new_expense/$', views.new_expense, name='new_expense'),
    # 用于编辑收入记录的网页
    re_path(r'^Record/edit_income/(?P<income_id>\d+)/$', views.edit_income, name='edit_income'),
    # 用于编辑支出记录的网页
    #re_path(r'^Record/edit_expense/(?P<expense_id>\d+)/$', views.edit_expense, name='edit_expense'),
]


"""产生的疑惑"""
# re_path中的name干什么用的？