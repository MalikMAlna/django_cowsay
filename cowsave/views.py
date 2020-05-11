from django.shortcuts import render, reverse, HttpResponseRedirect
from cowsave.forms import AddTextForm


def index(request):
    html = 'index.html'
    form = AddTextForm(request.POST)

    if request.method == "POST":
        form = AddTextForm(request.POST)
        if form.is_valid():
            form.cleaned_data

    return render(request, html, {"form": form})
