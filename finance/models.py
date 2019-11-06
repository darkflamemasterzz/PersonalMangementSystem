from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Income(models.Model):
    """收入"""
    incomeDate = models.DateTimeField()  # 收入日期
    incomeCount = models.IntegerField()  # 收入数目
    origin = models.CharField(max_length=50)  # 收入来源
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # 所对应的用户

    def __str__(self):
        """返回模型字符串表示"""
        return self.origin


class Expense(models.Model):
    """消费"""
    POCChoice = [
        ('p', 'Production'),
        ('c', 'Consume'),
    ]

    expenseDate = models.DateTimeField()  # 消费日期
    expenseCount = models.IntegerField()  # 消费数目
    target = models.CharField(max_length=50)  # 消费去向
    forProductionOrConsume = models.CharField(max_length=20, choices=POCChoice)  # 生产型支出还是消费型支出
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # 所对应的用户

    def __str__(self):
        """返回模型字符串表示"""
        return self.target
