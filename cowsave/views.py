from django.shortcuts import render
from django.views.generic import TemplateView
from cowsave.forms import AddTextForm
from cowsave.models import Text
import subprocess


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
            cowsave = subprocess.check_output(
                f'cowsay {text}', shell=True).decode("utf-8")
            # cowsave_list = list(cowsave)
            # cowsave_text = ""
            # for num in cowsave_list:
            #     cowsave_text += chr(num)
        form = AddTextForm()
        # cowsave = cowsave_text.split("\n")
        args = {"form": form, 'cowsave': cowsave}
        return render(request, self.template_name, args)


def history(request):
    html = 'history.html'
    text_list = list(Text.objects.all())
    texts = text_list[-10:][::-1]
    return render(request, html, {"texts": texts})
