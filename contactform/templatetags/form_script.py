import re

from django import template
from django.template import Context
from django.template.loader import render_to_string

from ..forms import ContactForm

register = template.Library()

@register.inclusion_tag('contact-form.html')
def form_tag():
    form = ContactForm()
    form.anti_spam()
    return {'contact_form':form}

@register.inclusion_tag('form-script.html')
def form_script():
    return {}