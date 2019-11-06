from django.shortcuts import render
from .models import Job, Project


# Create your views here.
def index(request):
    """工作模块主页"""
    return render(request, 'work/index.html')


def jobs(request):
    """列出工作列表"""
    jobs = Job.objects.order_by('title')
    context = {
        'jobs': jobs
    }
    return render(request, 'work/jobs.html', context)


def job(request, job_id):
    job = Job.objects.get(id=job_id)
    description = job.describe
    projects = Project.objects.filter(job=job)
    context = {
        'job': job,
        'description': description,
        'projects': projects,
    }
    return render(request, 'work/job.html', context)


def project(request, project_id):
    project = Project.objects.get(id=project_id)
    isDone = project.isDone
    range = project.range
    bodyText = project.bodyText
    startTime = project.startTime
    job = project.job
    context = {
        'project': project,
        'isDone': isDone,
        'range': range,
        'bodyText': bodyText,
        'startTime': startTime,
        'job': job,
    }
    return render(request, 'work/project.html', context)

