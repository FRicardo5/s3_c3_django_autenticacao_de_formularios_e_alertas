from django import forms

class LoginForms(forms.Form):
    nome_login = forms.CharField(
        label="nome de login",
        required=True,
        max_length=100
    )
    senha = forms.CharField(
        label="senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput()
    )