from django import forms
from django.contrib.auth.models import User
from .models import ServiceRequest


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', 'Passwords do not match.')
        return cleaned_data


class CheckoutForm(forms.Form):
    name = forms.CharField(max_length=200)
    phone = forms.CharField(max_length=20)
    address_line1 = forms.CharField(max_length=255)
    address_line2 = forms.CharField(max_length=255, required=False)
    city = forms.CharField(max_length=100, initial='Bengaluru')
    state = forms.CharField(max_length=100, initial='Karnataka')
    pincode = forms.CharField(max_length=10, initial='560001')
    payment_method = forms.ChoiceField(
        choices=[('COD', 'Cash on Delivery'), ('UPI', 'UPI (Coming Soon)')],
        initial='COD',
    )


class ServiceRequestForm(forms.ModelForm):
    BUDGET_CHOICES = [
        ('', 'Select Budget Range'),
        ('under_5k', 'Under ₹5,000'),
        ('5k_10k', '₹5,000 - ₹10,000'),
        ('10k_25k', '₹10,000 - ₹25,000'),
        ('25k_50k', '₹25,000 - ₹50,000'),
        ('above_50k', 'Above ₹50,000'),
    ]
    
    AREA_CHOICES = [
        ('', 'Select Area Size'),
        ('small', 'Small (Up to 100 sq ft)'),
        ('medium', 'Medium (100-300 sq ft)'),
        ('large', 'Large (300-500 sq ft)'),
        ('very_large', 'Very Large (Above 500 sq ft)'),
    ]
    
    budget = forms.ChoiceField(
        choices=BUDGET_CHOICES,
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    area_size = forms.ChoiceField(
        choices=AREA_CHOICES,
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    preferred_date = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        help_text='Preferred date for setup/consultation'
    )
    address = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        help_text='Full address for on-site service'
    )
    
    class Meta:
        model = ServiceRequest
        fields = ['name', 'email', 'phone', 'city', 'service_type', 'budget', 'area_size', 'preferred_date', 'address', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Full Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'your.email@example.com'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+91 XXXXX XXXXX'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Bengaluru, Mumbai, Delhi'}),
            'service_type': forms.Select(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Tell us about your requirements, space type (balcony/terrace/garden), sunlight availability, etc.'}),
        }
