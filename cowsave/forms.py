from django import forms


class AddTextForm(forms.Form):
    text = forms.CharField(max_length=5000, required=False)
