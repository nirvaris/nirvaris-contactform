import pdb,sys

from threading import Thread

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

        success='false'
        
        form = ContactForm(request.POST)
        
        form_valid = form.is_valid()
        cleaned_data = form.clean()

        if form_valid:
            
            try:
                form.save()
                thread = Thread(target=send_contact_message, args=(form.instance,))
                thread.start()
                form = ContactForm()
                success = 'true'
                messages.success(request,_("Thank you!! We can't wait to read it!"))
            except:

                messages.error(request,_('Sorry! We could not send your email.'))
        
        form_errors = form.errors.as_json()
        
        form.anti_spam()
        
        request_context = RequestContext(request,{'success':success,'form_errors':form_errors})

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
                thread = Thread(target=send_contact_message, args=(form.instance,))
                thread.start()
                form = ContactForm()
                messages.success(self.request,_("Thank you!! We can't wait to read it!"))
            except:
                #pdb.set_trace()                
                messages.error(self.request,_('Sorry! We could not send your email.'))
        
        form.anti_spam()
        
        request_context = RequestContext(request,{'form':form})

        return render_to_response('contact-form.html', request_context) 