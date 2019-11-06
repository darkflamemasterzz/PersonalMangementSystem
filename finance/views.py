from django.shortcuts import render
from .models import Income, Expense
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .form import IncomeForm, ExpenseForm


# Create your views here.
def index(request):
    """财务模块主页"""
    return render(request, 'finance/index.html')


@login_required()
def record(request):
    """显示所有收入和支出记录"""
    income = Income.objects.filter(user=request.user).order_by('incomeDate')
    expense = Expense.objects.filter(user=request.user).order_by('expenseDate')
    context = {
        'income': income,
        'expense': expense,
    }
    return render(request, 'finance/record.html', context)


@login_required()
def income(request, income_id):
    """显示详细单个收入记录"""
    income = Income.objects.filter(user=request.user).get(id=income_id)
    # 确认请求的收入词条属于当前用户
    if income.user != request.user:
        raise Http404
    incomeDate = income.incomeDate
    incomeCount = income.incomeCount
    context = {
        'income': income,
        'incomeDate': incomeDate,
        'incomeCount': incomeCount,
    }
    return render(request, 'finance/income.html', context)


@login_required()
def expense(request, expense_id):
    """显示详细单个支出记录"""
    expense = Expense.objects.filter(user=request.user).get(id=expense_id)
    # 确认请求的支出词条属于当前用户
    if expense.user != request.user:
        raise Http404
    expenseDate = expense.expenseDate
    expenseCount = expense.expenseCount
    forProductionOrConsume = expense.forProductionOrConsume
    context = {
        'expense': expense,
        'expenseDate': expenseDate,
        'expenseCount': expenseCount,
        'forProductionOrConsume': forProductionOrConsume,
    }
    return render(request, 'finance/expense.html', context)


@login_required()
def new_income(request):
    """添加新的收入记录"""
    if request.method != 'POST':
        # 未提交数据：创建一个新表单
        form = IncomeForm
    else:
        # POST提交的数据，对数据进行处理
        form = IncomeForm(request.POST)
        if form.is_valid():
            new_income = form.save(commit=False)
            new_income.user = request.user
            new_income.save()
            # form.save()
            return HttpResponseRedirect(reverse('finance:record'))

    context = {'form': form}
    return render(request, 'finance/new_income.html', context)


@login_required()
def new_expense(request):
    """添加新的支出记录"""
    if request.method != 'POST':
        # 未提交数据：创建新表单
        form = ExpenseForm
    else:
        # POST提交额数据，对数据进行处理
        # form = ExpenseForm(request.POST, initial={'user': request.user})
        form = ExpenseForm(request.POST)
        if form.is_valid():
            new_expense = form.save(commit=False)
            new_expense.user = request.user
            new_expense.save()
            # form.save()
            return HttpResponseRedirect(reverse('finance:record'))

    context = {'form': form}
    return render(request, 'finance/new_expense.html', context)


@login_required()
def edit_income(request, income_id):
    """编辑收入条目"""
    income = Income.objects.get(id=income_id)

    if request.method != 'POST':
        # 初次请求，使用当前收入条目填充表单
        form = IncomeForm(instance=income)  # instance?
    else:
        # POST提交的数据，对数据进行处理
        form = IncomeForm(instance=income, data=request.POST)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect(reverse('finance:income', args=[income.id]))
    context = {'income': income, 'form': form}
    return render(request, 'finance/edit_income.html', context)


"""遇到的坑"""
# 纠错器不准：unresolved objects in class Income..., 如何让它认得django?


"""产生的疑惑"""
# 1.对request不熟悉，它里面到底是什么？
