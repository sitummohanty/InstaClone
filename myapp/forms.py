from django import forms
from .models import User

class UserSignUpForm(forms.ModelForm):
    name = forms.CharField(
        required=True,
        widget=forms.TextInput(           # ← attrs go here
            attrs={
                "placeholder": "Enter your name",
                "class": "input_fields"
            }
        )
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                "placeholder": "you@example.com",
                "class": "input_fields"
            }
        )
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Create a password",
                "class": "input_fields"
            }
        )
    )

    class Meta:
        model   = User
        exclude = ('created_on', 'updated_on', 'is_active')