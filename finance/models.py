from django.db import models
from django.utils import timezone

class Transaction(models.Model):
    TYPE_CHOICES = (
        ('INCOME', 'Income'),
        ('EXPENSE', 'Expense'),
    )

    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(default=timezone.now)
    category = models.CharField(max_length=100)
    transaction_type = models.CharField(max_length=7, choices=TYPE_CHOICES)

    def __str__(self):
        return f"{self.description} - {self.amount}"

class SavingsGoal(models.Model):
    name = models.CharField(max_length=255)
    target_amount = models.DecimalField(max_digits=10, decimal_places=2)
    current_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.name

    @property
    def progress_percentage(self):
        if self.target_amount > 0:
            return min(int((self.current_amount / self.target_amount) * 100), 100)
        return 0
