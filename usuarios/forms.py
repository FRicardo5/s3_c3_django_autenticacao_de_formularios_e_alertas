from django import forms

class LoginForms(forms.Form):
    nome_login = forms.CharField(
        label="nome de login",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class" : "form-control",
                "placeholder" : "Ex: Felipe Ricardo"
            }
        )
    )
    senha = forms.CharField(
        label="senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class" : "form-control",
                "placeholder" : "Digite sua senha"
            }
        )
    )

class CadastroForms(forms.Form):
    nome_cadastro = forms.CharField(
        label="Nome de Cadastro",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class" : "form-control",
                "placeholder" : "Ex: Felipe Ricardo"
            }
        )
    )
    email = forms.EmailField(
    label="E-mail",
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                "class" : "form-control",
                "placeholder" : "Ex: felipe1ricardo158@gmail.com"
            }
        )
    )
    senha_1 = forms.CharField(
        label="senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class" : "form-control",
                "placeholder" : "Digite sua senha"
            }
        )
    )
    senha_2 = forms.CharField(
        label="senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class" : "form-control",
                "placeholder" : "Digite sua senha novamente"
            }
        )
    )

    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get("nome_cadastro")

        if nome:
            nome = nome.strip() # lembrete: método que retira espaços do inicio e fim da string
            if " " in nome:  # itera sobre a string procurando algum caracter "vazio"
                raise forms.ValidationError("Não é possível inserir espaços dentro do campo usuário")
            else:
                return nome