from django import forms


class UserForms(forms.Form):
    value1 = forms.CharField(label="Value 1", required=False, widget=forms.TextInput(attrs={'class':"form.control"}))
    value2 = forms.CharField(label="Value 2")
