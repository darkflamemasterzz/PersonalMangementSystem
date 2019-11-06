from django.db import models


# Create your models here.
class Book(models.Model):
    """书单"""
    fieldChoice = [
        ('cs', 'Computer Science'),
        ('phil', 'philosophy'),
        ('eco', 'economy'),
        ('pol', 'politics'),
    ]
    progressChoice = [
        ('0', '0%'),
        ('1', '0%~25%'),
        ('2', '25%~50%'),
        ('3', '50%~75%'),
        ('4', '75%~100%'),
    ]

    title = models.CharField(max_length=30)  # 书名
    author = models.CharField(max_length=20)  # 作者
    field = models.CharField(max_length=20, choices=fieldChoice)  # 领域
    description = models.CharField(max_length=100, null=True)  # 简述
    progress = models.CharField(max_length=20, choices=progressChoice)  # 阅读进度

    def __str__(self):
        """返回模型字符串表示"""
        return self.title


class Movie(models.Model):
    """电影清单"""
    title = models.CharField(max_length=30)  # 电影名
    director = models.CharField(max_length=30)  # 导演
    DateField = models.DateField()  # release date
    description = models.TextField(null=True)  # 简述
    review = models.TextField(null=True)  # 个人影评

    def __str__(self):
        """返回模型字符串表示"""
        return self.title


"""遇到的坑"""
# 我想省略不填简述和影片字段

"""有待完善的地方"""
# 补上出版日期
