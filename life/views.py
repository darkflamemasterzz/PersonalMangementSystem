from django.shortcuts import render
from .models import Log


# Create your views here.
def index(request):
    """生活模块主页"""
    return render(request, 'life/index.html')


def logs(request):
    """列出所有日志"""
    logs = Log.objects.order_by('date')
    context = {
        'logs': logs
    }
    return render(request, 'life/logs.html', context)


def log(request, log_id):
    log = Log.objects.get(id=log_id)
    Class = log.Class
    title = log.title
    date = log.date
    bodyText = log.bodyText
    context = {
        'log': log,
        'Class': Class,
        'title': title,
        'date': date,
        'bodyText': bodyText,
    }
    return render(request, 'life/log.html', context)


"""有待完善"""
# 1.实现filter功能
