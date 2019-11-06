from django.db import models


# Create your models here.
class Job(models.Model):
    """工作"""
    title = models.CharField(max_length=20)  # 标题
    describe = models.TextField()  # 工作描述

    def __str__(self):
        """返回模型字符串表示"""
        return self.title


class Project(models.Model):
    """工作计划"""
    timeRange = [
        ('y', 'Year'),
        ('m', 'Month'),
        ('w', 'Weak'),
        ('d', 'Day'),
    ]

    isDone = models.BooleanField()  # 是否已经完成了
    range = models.CharField(max_length=5, choices=timeRange)  # 年、月、周还是日计划
    title = models.CharField(max_length=20)  # 计划名称
    bodyText = models.CharField(max_length=50)  # 计划正文
    startTime = models.DateTimeField(auto_now_add=True)  # 计划创立时间
    # endTime = models.DateTimeField()  # 计划实际完成时间
    job = models.ForeignKey('Job', on_delete=models.CASCADE)

    def __str__(self):
        """返回模型字符串表示"""
        return self.title


"""遇到的坑"""
# 1.我想把project表中的job字段的选项内容设为job表的title (done)

"""有待完善"""
# 1.Job表应该有起始和结束字段
