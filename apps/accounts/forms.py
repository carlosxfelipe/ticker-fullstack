from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.ModelForm):
    email = forms.EmailField(label="E-mail")
    password = forms.CharField(label="Senha", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirme a senha", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["email", "password"]

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")
        if password and password2 and password != password2:
            self.add_error("password2", "As senhas não coincidem.")
        return cleaned_data
