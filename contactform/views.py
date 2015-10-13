import pdb

from django.contrib import messages
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.utils.translation import ugettext as _
from django.views.generic import TemplateView
from django.views.generic.base import View
# Create your views here.

from .email import send_contact_message
from .forms import ContactForm
from .models import ContactMessage


class ContactFormTag(TemplateView):
    template_name = "contact-form-tag.html"
    

class ContactFormView(View):

    
    def get(self, request):
        form = ContactForm()
        form.anti_spam()
        
        request_context = RequestContext(request,{'form':form})

        return render_to_response('contact-form.html', request_context)

    def post(self, request):
        form = ContactForm(request.POST)
        
        form_valid = form.is_valid()
        cleaned_data = form.clean()
        
        

        if form_valid:
            form.save()
            send_contact_message(request, form.instance)
            form = ContactForm()
            messages.success(self.request,_('Your message was sent'))
        
        form.anti_spam()
        
        request_context = RequestContext(request,{'form':form})

        return render_to_response('contact-form.html', request_context) 