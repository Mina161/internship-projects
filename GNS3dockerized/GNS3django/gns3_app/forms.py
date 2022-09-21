from django import forms

class RouterForm(forms.Form):
    name = forms.CharField(label='Router name', max_length=200)
    host = forms.CharField(label='Router host', max_length=100)
    port = forms.IntegerField(label='Port number', required=False)
    username = forms.CharField(label='Access username', max_length=200, required=False)
    password = forms.CharField(label='Access Password', max_length=200, required=False)
    secret = forms.CharField(label='Enable Password', max_length=200, required=False)
    