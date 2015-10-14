import pdb
import logging
from datetime import date

from django.conf import settings
from django.core.mail.message import EmailMessage
from django.template import RequestContext
from django.template.loader import render_to_string

from .models import ContactMessage

def send_contact_message(request, contact_message):
    
    dic_for_context = {}
    dic_for_context['name'] = contact_message.name
    dic_for_context['message'] = contact_message.message
    dic_for_context['email'] = contact_message.email
    dic_for_context['site_url'] = settings.SITE_URL
    context = RequestContext(request, dic_for_context)

    subject = render_to_string('contactform-email-subject.txt', context)
    template = render_to_string('contactform-email-body.html', context)

    msg = EmailMessage(subject, template, settings.EMAIL_FROM, [settings.EMAIL_TO_CONTACT])

    msg.content_subtype = "html"  
    msg.send()
    
    if contact_message.sen_to_me:
        msg = EmailMessage(subject, template, settings.EMAIL_FROM, [contact_message.email])

        msg.content_subtype = "html"  
        msg.send()        
    

