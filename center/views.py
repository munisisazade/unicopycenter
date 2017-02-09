from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from center.forms import UploadFileForm
# Create your views here.

class IndexRequestView(TemplateView,FormView):
    template_name = 'index.html'
    form_class = UploadFileForm


    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST,request.FILES)
        if form.is_valid():
            pass
        pass


    def get_context_data(self, **kwargs):
        context = super(IndexRequestView, self).get_context_data(**kwargs)
        context['html_lang'] = self.request.get_full_path()[1:3]
        return context

