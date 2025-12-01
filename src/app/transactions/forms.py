from django import forms

from .models import Transaction


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['item_name', 'amount', 'customer_name', 'category']
        widgets = {
            'item_name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'e.g., Latte, Cappuccino'
            }),
            'amount': forms.NumberInput(attrs={
                'class': 'form-input',
                'placeholder': '0.00',
                'step': '0.01'
            }),
            'customer_name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Optional'
            }),
            'category': forms.Select(attrs={
                'class': 'form-input'
            }),
        }
