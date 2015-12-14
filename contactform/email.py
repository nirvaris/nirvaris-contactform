import pdb, sys
import logging

from datetime import date

from django.conf import settings
from django.core.mail.message import EmailMessage
from django.template import RequestContext
from django.template.loader import render_to_string

from .models import ContactMessage

NV_CONTACTFORM_SUBJECT = 'Nirvaris Contact Form'

if hasattr(settings, 'NV_CONTACTFORM_SUBJECT'):
    if settings.NV_CONTACTFORM_SUBJECT:
        NV_CONTACTFORM_SUBJECT = settings.NV_CONTACTFORM_SUBJECT


def send_contact_message(contact_message):
    
    #pdb.set_trace()
    dic_for_context = {}
    dic_for_context['name'] = contact_message.name
    dic_for_context['message'] = contact_message.message
    dic_for_context['email'] = contact_message.email
    dic_for_context['product_name'] = NV_CONTACTFORM_SUBJECT

    #context = RequestContext(request, dic_for_context)

    subject = render_to_string('contact-form-email-subject.txt', dic_for_context)
    template = render_to_string('contact-form-email-body.html', dic_for_context)

    msg = EmailMessage(subject, template, settings.NV_EMAIL_FROM, [settings.NV_SEND_TO])

    msg.content_subtype = "html"  
    msg.send()
    
    if contact_message.send_to_me:
        msg = EmailMessage(subject, template, settings.NV_EMAIL_FROM, [contact_message.email])

        msg.content_subtype = "html"  
        msg.send()        
    

