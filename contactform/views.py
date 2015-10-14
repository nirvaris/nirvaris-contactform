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
    template_name = "test-contact-form-tag.html"
    
    def post(self, request):

        success='true'
        message=_('Your message was sent')
        
        form = ContactForm(request.POST)
        
        form_valid = form.is_valid()
        cleaned_data = form.clean()

        if form_valid:
            
            try:
                form.save()
                send_contact_message(request, form.instance)
                form = ContactForm()

            except:
                success='false'
                message=_('Ooops! We have some issues sending your e-mail')
        
        form.anti_spam()
        
        request_context = RequestContext(request,{'success':success,'message':message})

        return render_to_response('contact-form-tag-ajax.html', request_context, content_type='application/json') 

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
            
            try:
                form.save()
                send_contact_message(request, form.instance)
                form = ContactForm()
                messages.success(self.request,_('Your message was sent'))
            except:
                messages.error(self.request,_('Error sending your email'))
        
        form.anti_spam()
        
        request_context = RequestContext(request,{'form':form})

        return render_to_response('contact-form.html', request_context) 