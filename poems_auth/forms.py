from django import forms

class LoginModelFoms(forms.ModelForm):
    nome = forms.CharField(max_length=100)
    senha = forms.CharField(max_length=100)

class CadastroModelForms(forms.ModelForm):
    nome = forms.CharField(label="Nome", max_length=100)
    email = forms.EmailField(label="E-mail", max_length=100)
    senha = forms.CharField(label="Senha", max_length=100)