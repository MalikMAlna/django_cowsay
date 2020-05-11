from django.shortcuts import render
from django.views.generic import TemplateView
from cowsave.forms import AddTextForm
from cowsave.models import Text
# import subprocess


class HomeView(TemplateView):
    template_name = 'index.html'

    def get(self, request):
        form = AddTextForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = AddTextForm(request.POST)

        if form.is_valid():
            text = form.cleaned_data['text']
            Text.objects.create(
                text=text,
            )
            # cowsave = subprocess.run(f'cowsay {text}')
        form = AddTextForm()
        args = {"form": form, 'text': text}
        return render(request, self.template_name, args)


def history(request):
    html = 'history.html'
    text_list = list(Text.objects.all())
    texts = text_list[-10:][::-1]
    return render(request, html, {"texts": texts})
