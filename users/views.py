from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def logout_view(request):
    """注销用户"""
    logout(request)
    return HttpResponseRedirect(reverse('finance:index'))


def register(request):
    """注册新用户"""
    if request.method != 'POST':
        # 显示新的注册表单
        form = UserCreationForm()
    else:
        # 处理填写好的表单
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # 让用户自动登录，再重定向到主页
            authenticate_user = authenticate(username=new_user.username,
                                             password=request.POST['password1'])  # ?
            login(request, authenticate_user)
            return HttpResponseRedirect(reverse('finance:index'))

    context = {'form': form}
    return render(request, 'registration/register.html', context)


"""有待改善的地方"""
# 1.logout_view 应该重定向到主页或者用户登录器所在的页面的
