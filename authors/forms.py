from typing import Any
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


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

    def clean_password(self):
        data = self.cleaned_data.get("password")

        if "atenção" in data:
            raise ValidationError(
                "Não digite %(value)s no Password",
                code="invalid",
                params={"value": '"atenção"'},
            )

        return data

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            value = ValidationError(
                "Password and Confirm Password must be equal", code="invalid"
            )
            raise ValidationError(
                {
                    "password": value,
                    "confirm_password": value,
                }
            )
