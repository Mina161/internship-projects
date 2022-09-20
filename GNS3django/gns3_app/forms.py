from django import forms

class RouterForm(forms.Form):
    name = forms.CharField(label='Router name', max_length=200)
    ip = forms.CharField(label='Router IP address', max_length=16)
    username = forms.CharField(label='Access username', max_length=200, required=False)
    password = forms.CharField(label='Access Password', max_length=200, required=False)
    secret = forms.CharField(label='Enable Password', max_length=200, required=False)