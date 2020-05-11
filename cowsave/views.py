from django.shortcuts import render, reverse, HttpResponseRedirect
from django.views.generic import TemplateView
from cowsave.forms import AddTextForm


class HomeView(TemplateView):
    template_name = 'index.html'

    def get(self, request):
        form = AddTextForm()
        return render(request, self.template_name)

    def post(self, request):
        html = 'index.html'
        form = AddTextForm(request.POST)

        if request.method == "POST":
            form = AddTextForm(request.POST)
            if form.is_valid():
                text = form.cleaned_data['post']
                form = AddTextForm()

        args = {"form": form, 'text': text}
        return render(request, html, args)
