from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(label='Search')

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)