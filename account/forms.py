from django import forms


class LoginForm(forms.Form):
    """ Creating a login form for users and
    authenticate users against the database"""
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)