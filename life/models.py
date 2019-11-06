from django.db import models


# Create your models here.
class Log(models.Model):
    """日记"""
    ClassChoice = [
        ('d', 'Dairy'),
        ('qi', 'quick idea')
    ]

    Class = models.CharField(max_length=20, choices=ClassChoice)  # 是日记还是灵感
    title = models.CharField(max_length=50)  # 日记标题
    date = models.DateTimeField(auto_now_add=True)  # 时间
    bodyText = models.TextField(null=True)  # 日记正文

    def __str__(self):
        """返回模型字符串表示"""
        return self.title



