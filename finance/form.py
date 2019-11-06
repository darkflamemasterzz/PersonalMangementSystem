from django import forms
from .models import Income, Expense


class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['incomeDate', 'incomeCount', 'origin']


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['expenseDate', 'expenseCount', 'target', 'forProductionOrConsume']


"""有待改善"""
# 1.注册表单不应当让用户手动填写user字段的
