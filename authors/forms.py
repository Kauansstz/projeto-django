from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs["placeholder"] = "que legal"

    confirm_password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={"placeholder": "Confirm Password..."}),
        label="Confirm Password",
    )

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password",
        ]
        labels = {
            "username": "Username",
            "first_name": "First Name",
            "last_name": "Last Name",
            "email": "E-mail",
            "password": "Password",
        }
        widgets = {
            "first_name": forms.TextInput(attrs={"placeholder": "First Name..."}),
            "last_name": forms.TextInput(attrs={"placeholder": "Last Name..."}),
            "username": forms.TextInput(attrs={"placeholder": "Username..."}),
            "email": forms.TextInput(attrs={"placeholder": "E-mail..."}),
            "password": forms.PasswordInput(attrs={"placeholder": "Password..."}),
        }
