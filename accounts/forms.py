from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Address


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Email")
    first_name = forms.CharField(required=True, label="Prénom")
    last_name = forms.CharField(required=False, label="Nom")

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "username", "password1", "password2"]


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        exclude = ["user", "is_default", "created_at"]
        widgets = {
            "full_address": forms.Textarea(attrs={"rows": 2}),
        }
