from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum
from .models import Transaction, SavingsGoal

def dashboard(request):
    transactions = Transaction.objects.all().order_by('-date')[:5]
    goals = SavingsGoal.objects.all()
    
    total_income = Transaction.objects.filter(transaction_type='INCOME').aggregate(Sum('amount'))['amount__sum'] or 0
    total_expense = Transaction.objects.filter(transaction_type='EXPENSE').aggregate(Sum('amount'))['amount__sum'] or 0
    balance = total_income - total_expense
    
    context = {
        'transactions': transactions,
        'goals': goals,
        'balance': balance,
        'total_income': total_income,
        'total_expense': total_expense,
    }
    return render(request, 'finance/dashboard.html', context)

def transaction_list(request):
    transactions = Transaction.objects.all().order_by('-date')
    return render(request, 'finance/transaction_list.html', {'transactions': transactions})

def transaction_create(request):
    if request.method == 'POST':
        description = request.POST.get('description')
        amount = request.POST.get('amount')
        category = request.POST.get('category')
        transaction_type = request.POST.get('transaction_type')
        date = request.POST.get('date')
        
        Transaction.objects.create(
            description=description,
            amount=amount,
            category=category,
            transaction_type=transaction_type,
            date=date
        )
        return redirect('finance:transaction_list')
    return render(request, 'finance/transaction_form.html')

def transaction_delete(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    if request.method == 'POST':
        transaction.delete()
        return redirect('finance:transaction_list')
    return render(request, 'finance/transaction_confirm_delete.html', {'transaction': transaction})

def goal_list(request):
    goals = SavingsGoal.objects.all()
    return render(request, 'finance/goal_list.html', {'goals': goals})

def goal_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        target_amount = request.POST.get('target_amount')
        current_amount = request.POST.get('current_amount', 0)
        if not current_amount:
            current_amount = 0
            
        SavingsGoal.objects.create(
            name=name,
            target_amount=target_amount,
            current_amount=current_amount
        )
        return redirect('finance:goal_list')
    return render(request, 'finance/goal_form.html')
