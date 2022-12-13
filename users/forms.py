from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class':'txt_field'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'txt_field'
    }))


class RegisterForm(forms.Form):
    username = forms.CharField()
    password1 = forms.CharField(widget=forms.PasswordInput, min_length=5)
    password2 = forms.CharField(widget=forms.PasswordInput, min_length=5)
