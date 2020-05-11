from django import forms


class AddTextForm(forms.Form):
    text = forms.CharField(required=False)
