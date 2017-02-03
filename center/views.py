from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class IndexRequestView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexRequestView, self).get_context_data(**kwargs)
        context['html_lang'] = self.request.get_full_path()[1:3]
        return context