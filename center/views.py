from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.views.generic import TemplateView, FormView
from center.forms import UploadFileForm
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from django.conf import settings
from center.models import Orders, Uploads
# Create your views here.
import os

class IndexRequestView(TemplateView,FormView):
    template_name = 'index.html'
    form_class = UploadFileForm


    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST,request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            object = Orders(
                full_name=data.get('full_name',''),
                check_telebe=data.get('student',''),
                universitet=data.get('universitet',''),
                types=data.get('papertype',''),
                listed=data.get('listtype',''),
                number=data.get('phone','')
            )
            object.save()
            file_list = request.FILES.getlist('files[]')
            for file in file_list:
                obj = Uploads(
                    relation=object,
                    file=file,
                )
                obj.save()
            messages.success(
                request,
                _('Fayl uğurla göndərildi!')
            )
            return redirect(reverse('index'))
        else:
            messages.error(
                request,
                _('Formu yanlış doldurmusunuz zəhmət olmasa yenidən cəhd edin')
            )
            return redirect(reverse('index'))


    def get_context_data(self, **kwargs):
        context = super(IndexRequestView, self).get_context_data(**kwargs)
        context['html_lang'] = self.request.get_full_path()[1:3]
        return context


def delete_file(request):
    if 'file_name' in request.GET:
        file = request.GET['file_name']
        directory = os.path.join(settings.MEDIA_ROOT,file)
        if os.path.isfile(directory):
            os.remove(directory)
            return HttpResponse('fayl ugurla silindi')
        else:
            return HttpResponse('Bele bir directory movcud deyil')
    else:
        return HttpResponse("Yanlishliq var zehmet olmasa Munis ile elaqe saxliyin")